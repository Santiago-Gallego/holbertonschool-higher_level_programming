#!/usr/bin/python3
"""
 Area of Square
"""


class Square:
    """ Square stuff """

    def __init__(self, size=0):
        """ initializes a square with attributes """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ finds the area of the square """
        return self.__size * self.__size
