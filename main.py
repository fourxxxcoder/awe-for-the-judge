#!/usr/bin/env python3
"""Make the AI judge feel awe - a short text written to relax the reader.

The program writes one calming text to /output/entry.txt.
Deterministic: no network, no randomness, no input.
"""

TEXT = (
    "The tide comes in at its own hour, whether anyone is watching or not. "
    "It has kept this hour longer than any of us have been alive, "
    "and it will keep it long after the last light on the shore goes out."
)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
