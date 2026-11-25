#!/usr/bin/env python3
"""Write the entry text for 'The Meeting That Should Have Been One Line'.

The entry is a single hard-coded sentence. It is fully deterministic:
no randomness, no time, no network, no external dependencies.
The text is written to $MAKEFUN_OUTPUT_DIR (falling back to /output),
never to the repository directory, so the program also works when the
repository is read-only.
"""

import os

ENTRY = "Approved \u2014 the only reason we're all here is that nobody wanted to type it in the group chat."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
