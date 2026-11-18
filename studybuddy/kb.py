"""Load the scraped documents in data/ and find passages relevant to a question."""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_documents() -> dict[str, str]:
    return {p.stem: p.read_text(encoding="utf-8") for p in DATA_DIR.glob("*.txt")}


def search(question: str, k: int = 3) -> list[tuple[str, str]]:
    """Naive keyword-overlap retrieval; to be replaced with embeddings later."""
    words = set(question.lower().split())
    scored = []
    for name, text in load_documents().items():
        score = sum(text.lower().count(w) for w in words)
        if score:
            scored.append((score, name, text[:500]))
    scored.sort(reverse=True)
    return [(name, snippet) for _, name, snippet in scored[:k]]
