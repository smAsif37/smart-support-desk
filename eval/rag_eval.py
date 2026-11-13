"""Evaluate the RAG component.  Run from the repo root:

    python -m eval.rag_eval              # retrieval only (no API key needed)
    python -m eval.rag_eval --with-llm   # also checks the generated answers (needs GROQ_API_KEY)

Reports: retrieval hit@k, answer keyword accuracy, and out-of-scope rejection rate.
"""
import argparse
import json
from pathlib import Path

from app.rag import NOT_FOUND_TEXT, rag

HERE = Path(__file__).parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--with-llm", action="store_true")
    args = ap.parse_args()
    qa = json.loads((HERE / "rag_questions.json").read_text())
    oos = json.loads((HERE / "out_of_scope_questions.json").read_text())

    hit = ans_ok = 0
    rows = []
    for item in qa:
        hits = rag.retrieve(item["q"])
        got = any(h["source"] == item["source"] for h in hits)
        hit += got
        ok = None
        if args.with_llm:
            out = rag.answer(item["q"])
            ok = out["found"] and all(k.lower() in out["answer"].lower() for k in item["keywords"])
            ans_ok += bool(ok)
        rows.append((item["q"], got, hits[0]["score"] if hits else 0.0, ok))

    rejected = 0
    for q in oos:
        hits = rag.retrieve(q)
        if not hits:
            rejected += 1
        elif args.with_llm:
            rejected += not rag.answer(q)["found"]

    n = len(qa)
    print("| Question | Source retrieved | Top score | Answer correct |\n|---|---|---|---|")
    for q, got, sc, ok in rows:
        print(f"| {q} | {'yes' if got else 'NO'} | {sc:.2f} | {'-' if ok is None else ('yes' if ok else 'NO')} |")
    print(f"\nRetrieval hit@{4}: {hit}/{n} = {hit/n:.0%}")
    if args.with_llm:
        print(f"Answer accuracy (keyword match): {ans_ok}/{n} = {ans_ok/n:.0%}")
    print(f"Out-of-scope rejected: {rejected}/{len(oos)} = {rejected/len(oos):.0%}   (refusal text: '{NOT_FOUND_TEXT}')")


if __name__ == "__main__":
    main()
