#!/usr/bin/env python3
"""Famous Last Words at 1 Percent -- make.fun entry.

The program writes one line to /output/entry.txt: the funniest last
words a phone could say as its battery hits 1 percent.

The line is the phone itself talking, in its own voice, about its own
dying battery -- with a twist: it stayed at 1% on purpose, just to
watch its owner panic. No will reading, no goodbye to the charger,
no pun on 1 percent.
"""

import os
import sys

ENTRY = "I stayed at 1% for an hour on purpose, just to watch you panic. Best hour of my life."

# The grader runs the program in a sandbox where /output is writable.
# ENTRY_OUTPUT_DIR only exists so the line can be verified locally.
OUTPUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")


def main() -> int:
    text = ENTRY
    # The sealed scorer gates on 1-199 characters of non-blank UTF-8 text.
    # Refuse to write anything that would fail the gate.
    if not (1 <= len(text) <= 199) or not text.strip():
        print("entry fails the gate: must be 1-199 non-blank characters", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_DIR}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
