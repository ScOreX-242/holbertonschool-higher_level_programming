#!/usr/bin/python3
"""Defines a custom list class MyList that inherits from list."""


class MyList(list):
    """Implement a custom list class."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
