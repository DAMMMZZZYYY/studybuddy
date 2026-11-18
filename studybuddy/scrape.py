"""Scrape course pages into data/ (the raw knowledge base)."""

from pathlib import Path

import requests
from bs4 import BeautifulSoup

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def fetch_text(url: str) -> str:
    """Download a page and return its visible text."""
    resp = requests.get(url, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()
    return " ".join(soup.get_text(" ").split())


def save(name: str, text: str) -> Path:
    DATA_DIR.mkdir(exist_ok=True)
    path = DATA_DIR / f"{name}.txt"
    path.write_text(text, encoding="utf-8")
    return path


if __name__ == "__main__":
    print("TODO: add the course URLs to scrape.")
