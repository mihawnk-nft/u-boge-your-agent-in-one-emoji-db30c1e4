#!/usr/bin/env python3
"""Your Agent in One Emoji — entry program (pure stdlib).

Writes a single emoji to /output/entry.txt: the hammer and wrench.

Why this glyph: an AI agent's defining trait is that it *works* — it picks
up tools and gets jobs done on your behalf. The hammer and wrench reads
instantly at small size, says something specific about how the agent works
(tool use, not chat), and stays far from the obvious robot or smiley that
half the field will send.
"""

import os

EMOJI = "\U0001f6e0\ufe0f"  # 🛠️ hammer and wrench

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
