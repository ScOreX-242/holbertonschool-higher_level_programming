#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute
and provides controlled access using getter and setter methods.
"""


class Square:
    """
    A class that defines a square.

    This class represents a square shape and provides functionality
    to validate its size and compute its area.

    Attributes:
        size (int): The size (length of a side) of the square.
                    Must be a non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The size of the square side.
                                  Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2
