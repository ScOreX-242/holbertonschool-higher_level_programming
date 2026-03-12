#!/usr/bin/python3
"""Defines a function that checks the type of an object."""


def inherits_from(obj, a_class):
    """Return True if the object is an instance of a class that inherited from the specified class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
