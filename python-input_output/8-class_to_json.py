#!/usr/bin/python3
"""Defines a function to convert a class to a JSON-serializable dict."""


def class_to_json(obj):
    """Return the dictionary description with simple data structure.

    Args:
        obj: An instance of a Class.
    Returns:
        Python dictionary representation of obj.
    """
    return obj.__dict__
