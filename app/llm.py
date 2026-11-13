"""Thin wrapper around the Groq (OpenAI-compatible) chat API with real error handling."""
from typing import Dict, List, Optional

from . import config


class LLMError(RuntimeError):
    """Raised when the LLM provider is unreachable, misconfigured or returns nothing."""


_client = None


def _get_client():
    global _client
    if _client is None:
        if not config.GROQ_API_KEY:
            raise LLMError("GROQ_API_KEY is not set. Add it to .env or the Space secrets.")
        from openai import OpenAI
        _client = OpenAI(base_url=config.GROQ_BASE_URL, api_key=config.GROQ_API_KEY,
                         timeout=config.LLM_TIMEOUT, max_retries=2)
    return _client


def chat(messages: List[Dict[str, str]], temperature: float = 0.1, max_tokens: int = 700) -> str:
    kwargs = {}
    if config.LLM_MODEL.startswith("openai/gpt-oss"):
        kwargs["extra_body"] = {"reasoning_effort": "low"}  # keeps latency/cost down
    try:
        resp = _get_client().chat.completions.create(
            model=config.LLM_MODEL, temperature=temperature, max_tokens=max_tokens,
            messages=messages, **kwargs)
    except LLMError:
        raise
    except Exception as exc:  # network, auth, rate limit, bad model name ...
        raise LLMError(f"LLM request failed: {exc}") from exc
    content: Optional[str] = resp.choices[0].message.content if resp.choices else None
    if not content or not content.strip():
        raise LLMError("LLM returned an empty response.")
    return content.strip()
