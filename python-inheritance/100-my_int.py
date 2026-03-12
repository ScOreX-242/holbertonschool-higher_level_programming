#!/usr/bin/python3
"""Defines a rebellious integer class."""


class MyInt(int):
    """Invert == and != operators."""

    def __eq__(self, other):
        """Override == operator with != behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator with == behavior."""
        return super().__eq__(other)
