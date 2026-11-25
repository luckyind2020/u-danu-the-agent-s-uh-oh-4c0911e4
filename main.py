"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

The entry lives in entry.txt. This program loads it, checks it against the
bounty's own limits (exactly one word, at most 99 characters), and prints
it — the whole confession, unadorned.
"""

from pathlib import Path

MAX_CHARS = 99


def load_word(path: Path) -> str:
    """Read the entry word, stripping surrounding whitespace."""
    return path.read_text(encoding="utf-8").strip()


def validate(word: str) -> str:
    """Enforce the bounty rules: exactly one word, at most 99 characters."""
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if len(word) > MAX_CHARS:
        raise ValueError("entry must be at most 99 characters")
    return word


def main() -> None:
    print(validate(load_word(Path(__file__).with_name("entry.txt"))))


if __name__ == "__main__":
    main()
