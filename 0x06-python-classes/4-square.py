#!/usr/bin/python3
"""
 Area of Square
"""


class Square:
    """ Square stuff """

    def __init__(self, size=0):
        """ initializes a square with attributes """
        self.size = size

    @property
    def size(self):
        """ gets the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size with error handeling """
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ finds the area of the square """
        return self.__size * self.__size
