#!/usr/bin/python3
"""
Docstring for python-inheritance.7-base_geometry
"""


class BaseGeometry:
    """
    Docstring for BaseGeometry
    """
    def area(self):

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
