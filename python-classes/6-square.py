#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:  # Classe
    """Class that defines a square."""
    def __init__(self, size=0, position=(0, 0)):  # Méthode
        """Initializes a square with a given size and a position.

        Args:
            size: The size of the square.
            position: The position of a square.
        """
        self.size = size
        self.position = position

    def area(self):
        """Computes and returns the area of the square.

        The area is calculated using the size of the square
        multiplied by itself.
        """
        return self.size * self.size

    @property
    def size(self):
        """Getter for the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of the square.

        Args:
            value (int): size of the square, must be >= 0

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Attribut privé

    def my_print(self):
        """Prints the square with the character # and spaces to stdout.

        If size is 0, prints an empty line.
        """
        if self.size == 0:
            print()
            return
        for j in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    @property
    def position(self):
        """Getter for the position of the square.

        Returns:
            tuple: the current position (tuple of 2 positive integers)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position of the square.

        Args:
            value (tuple): a tuple of 2 positive integers

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
