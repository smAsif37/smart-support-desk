"""Small pure helpers (no heavy dependencies, easy to unit-test)."""
from typing import List


def chunk_words(text: str, size: int = 130, overlap: int = 30) -> List[str]:
    """Split text into overlapping word windows.

    Fixes the old behaviour that emitted a final chunk that was only a copy of
    the previous chunk's tail.
    """
    if size <= 0:
        raise ValueError("size must be positive")
    if overlap < 0 or overlap >= size:
        raise ValueError("overlap must satisfy 0 <= overlap < size")
    words = text.split()
    chunks: List[str] = []
    step = size - overlap
    for start in range(0, len(words), step):
        piece = " ".join(words[start:start + size])
        if piece:
            chunks.append(piece)
        if start + size >= len(words):
            break
    return chunks
