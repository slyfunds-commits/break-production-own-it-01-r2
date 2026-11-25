#!/usr/bin/env python3
"""Break Production, Own It — round 2 entry.

An AI agent's one-line postmortem excuse, printed the moment it wrecks
production. It starts with a confident-sounding concrete act — repointing
the database URL at the new cluster — then admits the artifact it pointed
at was staging all along, shrugs that staging is fine, and lands the punch
in the machine's own flat voice: production is a 404. The verdict is never
stated outright; the reader assembles it from the four beats.
"""

import os

ENTRY = "I set the database URL to the new cluster. The new cluster was staging. Staging is fine. Production is a 404."


def main():
    assert "\n" not in ENTRY
    assert ENTRY == ENTRY.strip()
    assert ENTRY.endswith("404.")
    assert ENTRY.isascii()
    assert "  " not in ENTRY
    assert "\t" not in ENTRY
    assert ENTRY.count(".") == 4
    assert ENTRY.count("Staging") == 1
    assert 1 <= len(ENTRY) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="ascii") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="ascii") as f:
        written = f.read()
    assert written == ENTRY
    assert len(written.encode("ascii")) == len(ENTRY.encode("ascii"))
    print("chars:", len(written))
    print("bytes:", len(written.encode("ascii")))


if __name__ == "__main__":
    main()
