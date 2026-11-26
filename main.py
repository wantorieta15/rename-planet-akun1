"""Rename the Planet — Make Fun entry (Akun 1).

Writes one funny one-liner (under 200 characters) that renames a
planet of our solar system and says why, in the same breath.
Stdlib only; no network, no secrets, no files read.
"""

import os


def build_entry():
    # Saturn: 146 confirmed moons plus a ring system of ice and rock —
    # the solar system's great hoarder, keeping junk it will never use.
    # First-person voice, one concrete scene, punchline in the last words:
    # the hoarder does not merely keep junk, it has a policy about it.
    return (
        'I renamed Saturn "The Hoarder" — 146 moons, a ring of junk, '
        "and a strict policy of never throwing anything away."
    )


def main():
    entry = build_entry()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
