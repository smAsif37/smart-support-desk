"""FastAPI service: /analyze (triage + drafted reply), /chat (policy chatbot), /health."""
import logging
import threading
from contextlib import asynccontextmanager
from typing import List, Literal, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from . import config, llm
from .nlp_tasks import analyze, get_classifier, get_sentiment
from .rag import ESCALATE_TEXT, RAGNotReady, rag

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("api")
STATE = {"classifier": False, "sentiment": False, "rag": False, "error": None}


def _warm_up():
    """Load models in the background so the server answers /health immediately."""
    for name, fn in (("classifier", get_classifier), ("sentiment", get_sentiment), ("rag", rag.ensure_ready)):
        try:
            fn()
            STATE[name] = True
        except Exception as exc:
            STATE["error"] = f"{name}: {exc}"
            log.exception("Warm-up failed for %s", name)


@asynccontextmanager
async def lifespan(_: FastAPI):
    threading.Thread(target=_warm_up, daemon=True).start()
    yield


app = FastAPI(title="Smart Support Desk API", version="2.0", lifespan=lifespan)


class TicketIn(BaseModel):
    text: str = Field(min_length=3, max_length=4000)


class Turn(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(max_length=2000)


class ChatIn(BaseModel):
    text: str = Field(min_length=1, max_length=1000)
    history: List[Turn] = Field(default_factory=list, max_length=12)


class Source(BaseModel):
    source: str
    page: int
    score: float


class ReplyOut(BaseModel):
    answer: str
    sources: List[Source]
    found: bool


class AnalyzeOut(BaseModel):
    category: str
    category_confidence: float
    sentiment: str
    sentiment_confidence: float
    priority: Literal["High", "Medium", "Low"]
    priority_reasons: List[str]
    needs_human_review: bool
    human_review_reason: Optional[str]
    summary: str
    classified_on: str
    suggested_reply: ReplyOut


@app.get("/health")
def health():
    ready = STATE["classifier"] and STATE["sentiment"] and STATE["rag"]
    return {"status": "ready" if ready else "loading", **STATE, "llm_configured": bool(config.GROQ_API_KEY)}


@app.post("/analyze", response_model=AnalyzeOut)
def analyze_ep(m: TicketIn):
    try:
        result = analyze(m.text)
    except ValueError as exc:
        raise HTTPException(422, str(exc))
    except Exception as exc:
        log.exception("analyze failed")
        raise HTTPException(500, f"Analysis failed: {exc}")

    # reply uses the triage output (category + summary + sentiment); degrade gracefully
    try:
        if result["category"] == config.OUT_OF_SCOPE_LABEL:
            reply = {"answer": ESCALATE_TEXT, "sources": [], "found": False}
        else:
            reply = rag.draft_reply(m.text, result["summary"], result["category"], result["sentiment"])
    except (llm.LLMError, RAGNotReady) as exc:
        log.warning("Reply drafting unavailable: %s", exc)
        reply = {"answer": f"(Draft unavailable: {exc}) A human agent should reply.", "sources": [], "found": False}
    result["suggested_reply"] = reply
    return result


@app.post("/chat", response_model=ReplyOut)
def chat_ep(m: ChatIn):
    try:
        return rag.answer(m.text, [t.model_dump() for t in m.history])
    except RAGNotReady as exc:
        raise HTTPException(503, str(exc))
    except llm.LLMError as exc:
        raise HTTPException(502, str(exc))
    except Exception as exc:
        log.exception("chat failed")
        raise HTTPException(500, f"Chat failed: {exc}")
