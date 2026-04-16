#!/usr/bin/python3
'''This module writes to file.'''


def write_file(filename="", text=""):
    """Writes to file."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
