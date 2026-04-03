#!/usr/bin/python3
"""
Module: rectangle

This module defines a Rectangle class that represents a rectangle
with a given width and height.
"""


class Rectangle:
    """
    A class used to represent a rectangle.

    Attributes:
        width (int): The width of the rectangle (must be >= 0).
        height (int): The height of the rectangle (must be >= 0).
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        The area is computed as:
            width * height

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        The perimeter is computed as:
            2 * (width + height)

        If either width or height is 0, the perimeter is 0.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return self.__height * 2 + self.__width * 2
      
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_lines = []
        for i in range(self.__height):
            rectangle_lines.append("#" * self.__width)
        return "\n".join(rectangle_lines)
