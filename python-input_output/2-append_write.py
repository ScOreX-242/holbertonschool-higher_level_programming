#!/usr/bin/python3
'''This module appends to file.'''


def append_write(filename="", text=""):
    """Appends to file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
