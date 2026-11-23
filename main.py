#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry "A" (coffee).

The whole entry is a single letter: A stands for coffee. This program
writes exactly that one byte to the grader's output path, nothing more.
No trailing newline, no extra whitespace — the gate accepts only a
file of exactly one character.
"""

from os import environ, makedirs
from os.path import dirname

LETTER = b"A"
OUTPUT_PATH = environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def write_letter(path: str = OUTPUT_PATH) -> None:
    folder = dirname(path)
    if folder:
        makedirs(folder, exist_ok=True)
    with open(path, "wb") as out:
        out.write(LETTER)


if __name__ == "__main__":
    write_letter()
