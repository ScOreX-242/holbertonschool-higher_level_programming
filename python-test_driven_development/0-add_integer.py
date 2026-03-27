#!/usr/bin/python3
"""
0-add_integer module
This module provides a function that adds two integers.

"""


def add_integer(a, b=98):
    """
    Adds two integers a and b.
    If a or b is a float, it is casted to an int before addition.
    """
    # Check if a is exactly an int or float
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    # Check if b is exactly an int or float
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    # Cast to int and return the addition
    return int(a) + int(b)
