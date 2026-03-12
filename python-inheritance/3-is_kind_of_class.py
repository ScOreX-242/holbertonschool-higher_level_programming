#!/usr/bin/python3
"""Defines a function that checks the type of an object."""


def is_kind_of_class(obj, a_class):
    """Return True if the object is an instance of the specified class."""
    return isinstance(obj, a_class)
