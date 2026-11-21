"""The joke the reviewer laughs at -- make.fun entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (1-280 chars, UTF-8). Deterministic, standard library
only, no network. The entry is a single fixed text: the program's job is
to deliver it byte-for-byte, every run.
"""

import os
import sys

JOKE = "I told my agent to keep it simple. It deleted the whole codebase and left a README that says 'simple now'."

MAX_CHARS = 280


def validate(text):
    points = len(text)
    if points < 1 or points > MAX_CHARS:
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, points))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    text = validate(JOKE)
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise ValueError("entry.txt does not match the joke byte-for-byte")
    return 0


if __name__ == "__main__":
    sys.exit(main())
