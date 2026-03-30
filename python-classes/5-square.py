#!/usr/bin/python3
"""
Module: square

This module defines a class that represents a square and provides
basic operations such as computing its area and printing it
using a specific character representation.

The module does not rely on any external imports and is designed
to demonstrate encapsulation, property validation, and simple
class behavior in Python.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
        size (int): The size (length of a side) of the square.
                    Must be a non-negative integer.

    Methods:
        area():
            Returns the area of the square.

        my_print():
            Prints the square using the character '#'.
            If size is 0, prints an empty line.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
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
            ValueError: If value is negative.
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
            int: The area (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character.

        If size is 0, prints an empty line.
        Otherwise, prints a square of size x size.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

