#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day — make.fun entry.

Writes one original one-line roast of a daily gadget to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the variable
is unset).

Python 3.13, standard library only, no network access, fully deterministic:
every run writes exactly the same bytes.
"""

import os

# The entry: one line, 116 characters, inside the 1-200 gate.
# The roast targets the phone everyone unlocks a hundred times a day:
# Face ID knows you instantly, yet the phone still demands the password
# every morning — the punchline being that even the phone does not
# trust you before coffee.
ENTRY = (
    "My phone unlocks with my face but still asks for my password "
    "every morning \u2014 even it doesn\u2019t trust me before coffee."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry must not be empty or only whitespace")
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise SystemExit("entry must not contain control characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
