"""Explainable ticket priority. Replaces the old 'sentiment -> priority' lookup."""
from typing import List, Tuple

SECURITY_TERMS = ("hacked", "unauthorized", "unauthorised", "fraud", "stolen", "compromised",
                  "phishing", "someone logged", "not me who", "scam")
URGENCY_TERMS = ("urgent", "asap", "immediately", "right now", "today itself", "lawyer", "legal action",
                 "consumer court", "chargeback", "police", "escalate")
MONEY_TERMS = ("charged twice", "double charged", "deducted", "money debited", "money was taken",
               "overcharged", "wrong amount")
MONEY_CATEGORIES = {"PAYMENT", "REFUND", "INVOICE"}
SENTIMENT_POINTS = {"negative": 2, "neutral": 1, "positive": 0}


def _has_any(text: str, terms: Tuple[str, ...]) -> List[str]:
    return [t for t in terms if t in text]


def compute_priority(category: str, sentiment: str, text: str) -> Tuple[str, List[str]]:
    """Return (priority, reasons). Security problems are always High."""
    low = text.lower()
    reasons: List[str] = []

    sec = _has_any(low, SECURITY_TERMS)
    if sec:
        return "High", [f"security keyword: '{sec[0]}'"]

    score = SENTIMENT_POINTS.get(sentiment.lower(), 1)
    if score == 2:
        reasons.append("negative sentiment")

    urgent = _has_any(low, URGENCY_TERMS)
    if urgent:
        score += 2
        reasons.append(f"urgency/escalation wording: '{urgent[0]}'")

    money = _has_any(low, MONEY_TERMS)
    if money:
        score += 2
        reasons.append(f"possible money problem: '{money[0]}'")
    elif category.upper() in MONEY_CATEGORIES:
        score += 1
        reasons.append(f"financial category ({category.upper()})")

    if score >= 4:
        priority = "High"
    elif score >= 2:
        priority = "Medium"
    else:
        priority = "Low"
    if not reasons:
        reasons.append("no risk signals found")
    return priority, reasons
