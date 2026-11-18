"""StudyBuddy command-line bot."""

from studybuddy import kb


def answer(question: str) -> str:
    hits = kb.search(question)
    if not hits:
        return "I couldn't find that in the course material. Please check with your lecturer."
    sources = ", ".join(name for name, _ in hits)
    return f"{hits[0][1]}\n\n(Sources: {sources})"


def main() -> None:
    print("StudyBuddy ready. Type 'quit' to exit.")
    while True:
        try:
            q = input("> ").strip().lstrip("﻿")
        except (EOFError, KeyboardInterrupt):
            break
        if q.lower() in {"quit", "exit"}:
            break
        if q:
            print(answer(q))


if __name__ == "__main__":
    main()
