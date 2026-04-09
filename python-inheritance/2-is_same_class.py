#!/usr/bin/python3
    """
    Checks if `obj` is exactly an instance of the specified class

    Args:
        obj (any): The object to compare
        a_class (any): The class to compare with the object

    Returns:
        `True` if the object is exactly an instance of the
        specified class; otherwise `False`
    """


def is_same_class(obj, a_class):
  return type(obj) is a_class
