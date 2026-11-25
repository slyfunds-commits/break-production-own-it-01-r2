#!/usr/bin/env python3
"""Break Production, Own It — R2 (final round) entry.

Writes the keeper line to /output/entry.txt. Pure Python stdlib only
(the grader runs python:3.13-slim with no site-packages).

The line: an AI agent's one-line postmortem excuse, printed the instant
it breaks production. It owns the specific act in the first beat
("I set the database URL to the new cluster"), excuses via the cluster
it pointed at in the second ("The new cluster was staging"), adds the
deadpan second beat ("Staging is fine"), and the last beat lands on the
machine-voiced error code — the reader completes the verdict: prod now
points at staging, so production is a 404.
"""

import os

ENTRY = "I set the database URL to the new cluster. The new cluster was staging. Staging is fine. Production is a 404."


def main():
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not start/end with whitespace"
    assert ENTRY.endswith("404."), "punch word must be the last word"
    assert ENTRY.isascii(), "entry must be plain ASCII so bytes == chars"
    assert "  " not in ENTRY, "entry must not contain double spaces"
    assert ENTRY.count(".") == 4, "entry must be four beats, four periods"
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200 gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "byte mismatch after write"
    assert len(written.encode("utf-8")) == len(ENTRY.encode("utf-8"))
    print(f"entry.txt written: {len(written)} chars, {len(written.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
