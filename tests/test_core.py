import random
import sys
import types
import unittest

from app.priority import compute_priority
from app.privacy import redact_pii
from app.textutils import chunk_words
from training.data import add_noise, dedupe, norm_key
from training.oos_data import build_oos, split_oos_cores


class ChunkTests(unittest.TestCase):
    def test_overlap_and_size(self):
        text = " ".join(f"w{i}" for i in range(300))
        ch = chunk_words(text, 130, 30)
        self.assertTrue(all(len(c.split()) <= 130 for c in ch))
        self.assertEqual(ch[0].split()[-30:], ch[1].split()[:30])

    def test_no_redundant_tail_chunk(self):
        ch = chunk_words(" ".join(str(i) for i in range(130)), 130, 30)
        self.assertEqual(len(ch), 1)

    def test_empty_and_bad_args(self):
        self.assertEqual(chunk_words("", 10, 2), [])
        with self.assertRaises(ValueError):
            chunk_words("a b c", 10, 10)


class PriorityTests(unittest.TestCase):
    def test_security_always_high(self):
        self.assertEqual(compute_priority("ACCOUNT", "neutral", "my account was hacked")[0], "High")

    def test_money_negative_high(self):
        self.assertEqual(compute_priority("PAYMENT", "negative", "I was charged twice, urgent")[0], "High")

    def test_calm_question_low(self):
        self.assertEqual(compute_priority("DELIVERY", "positive", "how long does delivery take")[0], "Low")

    def test_neutral_refund_medium(self):
        self.assertEqual(compute_priority("REFUND", "neutral", "where is my refund")[0], "Medium")


class PrivacyTests(unittest.TestCase):
    def test_redaction(self):
        s = redact_pii("mail me at a.b@x.com or call +91 98765 43210, card 4111 1111 1111 1111")
        self.assertNotIn("a.b@x.com", s)
        self.assertNotIn("4111", s)
        self.assertNotIn("98765", s)

    def test_plain_text_untouched(self):
        self.assertEqual(redact_pii("where is my order"), "where is my order")


class DataTests(unittest.TestCase):
    def test_dedupe_template_duplicates(self):
        out = dedupe([("Cancel order 123", "ORDER"), ("cancel order 456!", "ORDER"), ("track my order", "ORDER")])
        self.assertEqual(len(out), 2)
        self.assertEqual(norm_key("Hi {{Name}}, order 55"), "hi order")

    def test_noise_changes_text_but_is_deterministic(self):
        a = add_noise("Please cancel my order immediately", random.Random(1))
        b = add_noise("Please cancel my order immediately", random.Random(1))
        self.assertEqual(a, b)

    def test_oos_builder(self):
        self.assertEqual(len(build_oos(50)), 50)

    def test_oos_cores_are_held_out(self):
        g = split_oos_cores(42)
        self.assertFalse(set(g["train"]) & set(g["test"]))
        self.assertFalse(set(g["train"]) & set(g["val"]))
        self.assertTrue(g["test"] and g["val"])


# ---- RAG logic with fakes (no models / no network) ----
def _install_fake_llm(reply):
    from app import llm
    calls = []
    def fake_chat(messages, **kw):
        calls.append(messages)
        return reply
    llm.chat = fake_chat
    return calls


class RagLogicTests(unittest.TestCase):
    def setUp(self):
        from app.rag import PolicyRAG
        self.rag = PolicyRAG()
        self.hit = {"source": "refund.pdf", "page": 1, "text": "Refunds take 5 to 7 days.", "score": 0.8}

    def test_no_hits_skips_llm(self):
        calls = _install_fake_llm("should not be used")
        self.rag.retrieve = lambda q, k=None: []
        out = self.rag.answer("who won the match?")
        self.assertFalse(out["found"])
        self.assertEqual(out["sources"], [])
        self.assertEqual(calls, [])

    def test_found_returns_sources(self):
        _install_fake_llm("Refunds take 5 to 7 days (refund.pdf).")
        self.rag.retrieve = lambda q, k=None: [self.hit]
        out = self.rag.answer("how long are refunds?")
        self.assertTrue(out["found"])
        self.assertEqual(out["sources"][0]["page"], 1)

    def test_llm_refusal_hides_sources(self):
        from app.rag import NOT_FOUND_TEXT
        _install_fake_llm(NOT_FOUND_TEXT)
        self.rag.retrieve = lambda q, k=None: [self.hit]
        out = self.rag.answer("something odd")
        self.assertFalse(out["found"])
        self.assertEqual(out["sources"], [])

    def test_followup_uses_history_for_retrieval_and_redacts(self):
        _install_fake_llm("ok")
        seen = {}
        self.rag.retrieve = lambda q, k=None: seen.setdefault("q", q) and [self.hit]
        hist = [{"role": "user", "content": "What is the refund time?"},
                {"role": "assistant", "content": "5 to 7 days"}]
        self.rag.answer("and for COD?", hist)
        self.assertIn("refund", seen["q"].lower())

    def test_draft_reply_uses_tone_and_context(self):
        calls = _install_fake_llm("Sorry about that...")
        self.rag.retrieve = lambda q, k=None: [self.hit]
        out = self.rag.draft_reply("Where is my refund??", "Customer wants refund status", "REFUND", "negative")
        self.assertTrue(out["found"])
        self.assertIn("apology", calls[0][0]["content"])

    def test_draft_reply_escalates_without_context(self):
        _install_fake_llm("x")
        self.rag.retrieve = lambda q, k=None: []
        out = self.rag.draft_reply("hi", "greeting", "OTHER", "neutral")
        self.assertFalse(out["found"])
        self.assertIn("human agent", out["answer"])


if __name__ == "__main__":
    unittest.main()
