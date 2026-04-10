#!/usr/bin/python3
"""Module for SwimMixin, FlyMixin, and Dragon classes."""


class SwimMixin:
    """Mixin for swimming ability."""

    def swim(self):
        """Print swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin for flying ability."""

    def fly(self):
        """Print flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class with swimming and flying abilities."""

    def roar(self):
        """Print roaring message."""
        print("The dragon roars!")
