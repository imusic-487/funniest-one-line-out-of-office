"""Funniest one-line out-of-office reply.

Writes a single line (94 characters) to /output/entry.txt.
The line is a genuine out-of-office message with a fresh twist:
the auto-reply itself has taken over the sender's job.
"""

from pathlib import Path

ENTRY = "I'm out of office \u2014 this auto-reply is now doing my job, and so far my manager hasn't noticed."


def main() -> None:
    # Gate: one line, 1-160 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be a single non-blank line"
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
