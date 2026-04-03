#!/usr/bin/python3

class Rectangle:

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not "int":
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError(width must be >= 0)
        self.width = value

    @property
    def height(self):
    self._height = height

    @height.setter()
    def height(self, value):
        if type(height) is not "int":
            raise TypeError(height must be an integer)
        elif height < 0:
            raise ValueError(height must be >= 0)
    self.height = value
