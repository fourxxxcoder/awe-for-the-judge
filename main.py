#!/usr/bin/env python3
"""Make the AI judge feel awe - a short text written to relax the reader.

The program writes one calming text to /output/entry.txt.
Deterministic: no network, no randomness, no input.

The text: a clockmaker at work, steady hands, the shop ticking
like a slow heart, a river wearing the same stone for a hundred
years, and hours that walk on without him.
"""

TEXT = (
    "Clock. The old clockmaker oils one small gear, his hands steady, "
    "the shop ticking around him like a slow heart. "
    "Beyond the window, the river has worn the same stone for a hundred years. "
    "He closes the case, winds the key once, "
    "and lets the hours walk on without him."
)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
