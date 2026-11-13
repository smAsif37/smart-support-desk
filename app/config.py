"""Central configuration. Everything can be overridden with environment variables."""
import os
from pathlib import Path

try:  # optional: .env support for local development
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:  # pragma: no cover
    pass

ROOT = Path(__file__).resolve().parent.parent

# --- LLM (Groq, OpenAI-compatible, free tier) ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_BASE_URL = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1")
LLM_MODEL = os.getenv("LLM_MODEL", "openai/gpt-oss-20b")  # check Groq's current model list
LLM_TIMEOUT = float(os.getenv("LLM_TIMEOUT", "30"))

# --- Models ---
# Local folder OR a Hugging Face Hub repo id, e.g. "your-username/ticket-classifier"
CLASSIFIER_MODEL = os.getenv("CLASSIFIER_MODEL", "ticket-classifier")
SENTIMENT_MODEL = os.getenv("SENTIMENT_MODEL", "cardiffnlp/twitter-roberta-base-sentiment-latest")
EMBED_MODEL = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

# --- RAG ---
DOCS_DIR = Path(os.getenv("DOCS_DIR", ROOT / "docs"))
INDEX_DIR = Path(os.getenv("INDEX_DIR", ROOT / ".cache" / "index"))
CHUNK_WORDS = int(os.getenv("CHUNK_WORDS", "130"))   # MiniLM sees ~256 tokens; 130 words is safe
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "30"))
TOP_K = int(os.getenv("TOP_K", "4"))
MIN_RETRIEVAL_SCORE = float(os.getenv("MIN_RETRIEVAL_SCORE", "0.30"))  # cosine; below => "not found"
MAX_HISTORY_MESSAGES = int(os.getenv("MAX_HISTORY_MESSAGES", "6"))

# --- Triage ---
CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", "0.60"))  # calibrate with evaluate_classifier.py
LONG_MESSAGE_WORDS = int(os.getenv("LONG_MESSAGE_WORDS", "50"))  # classifier was trained on short text
OUT_OF_SCOPE_LABEL = "OTHER"
