"""Lightweight PII redaction applied BEFORE any text leaves our servers (LLM API calls)."""
import re

_EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
_CARD = re.compile(r"\b(?:\d[ -]?){13,19}\b")
_AADHAAR = re.compile(r"\b\d{4}\s\d{4}\s\d{4}\b")
_PHONE = re.compile(r"(?<!\w)(?:\+?\d{1,3}[\s.-]?)?(?:\(?\d{2,5}\)?[\s.-]?)\d{3,5}[\s.-]?\d{3,5}(?!\w)")


def redact_pii(text: str) -> str:
    """Replace emails, card numbers, Aadhaar-style IDs and phone numbers with tags.

    Order matters: long digit runs (cards, IDs) are handled before phones.
    This is a safety net, not a guarantee; see the report's Reflect section.
    """
    text = _EMAIL.sub("[EMAIL]", text)
    text = _CARD.sub("[CARD]", text)
    text = _AADHAAR.sub("[ID]", text)
    text = _PHONE.sub("[PHONE]", text)
    return text
