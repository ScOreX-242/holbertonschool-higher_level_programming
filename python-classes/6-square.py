#!/usr/bin/python3
"""
Module: square

This module defines a Square class that represents a square with
a given size and position.

Features:
- Encapsulation via private attributes (__size, __position)
- Validation through property setters
- Area calculation
- Formatted printing with positional offsets

The module does not use any external libraries.
"""

class Square:
    """
    Represents a square with a given size and position.

    Attributes:
        size (int): Length of a side of the square.
                    Must be a non-negative integer.

        position (tuple): A tuple of 2 non-negative integers:
                          (horizontal_offset, vertical_offset)
                          used for printing the square.

    Methods:
        area():
            Returns the area of the square.

        my_print():
            Prints the square using '#' characters,
            respecting the position offsets.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): Size of the square. Defaults to 0.
            position (tuple, optional): Tuple of 2 non-negative integers
                                       representing print offsets.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
            TypeError: If position is not a valid tuple of 2 non-negative integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: Current size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): New size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            tuple: (horizontal_offset, vertical_offset)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Args:
            value (tuple): Tuple of 2 non-negative integers.

        Raises:
            TypeError: If value is not a tuple of 2 non-negative integers.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: size squared.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters with position offsets.

        Behavior:
        - If size == 0: prints an empty line.
        - Prints vertical offset (empty lines) first.
        - Then prints the square with horizontal offset (spaces before '#').

        Example:
            size = 2, position = (2, 1)

            Output:

              ##
              ##
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
