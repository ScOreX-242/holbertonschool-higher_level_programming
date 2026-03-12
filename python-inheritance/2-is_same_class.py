#!/usr/bin/python3
"""Defines a function that checks the type of an object."""


def is_same_class(obj, a_class):
    """Return True if the object is exactly an instance of the specified class."""
    return type(obj) is a_class
