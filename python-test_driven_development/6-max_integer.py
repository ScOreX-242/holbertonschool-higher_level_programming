#!/usr/bin/python3
"""Defines a max-finding function."""


def max_integer(list=[]):
    """Return the max integer in a list of integers.

    If the list is empty, return None.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
