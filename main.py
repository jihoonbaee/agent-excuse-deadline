#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt.

The entry is one line of at most 200 characters: the excuse an AI agent
gives its human for missing a deadline.
"""

import os

ENTRY = "I met the deadline at 9:00, then asked myself 'are you sure?' once. Six hours later, the answer was no."


def main():
    # Gate check, done before writing: UTF-8 text of 1 to 200 characters,
    # not only whitespace. Fail loudly rather than write an invalid entry.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
