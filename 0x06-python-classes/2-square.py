#!/usr/bin/python3
"""
 Square Class: Private Instance Vairable size with optional
"""


class Square:
    """ Private instance variable size with optinals """

    def __init__(self, size=0):
        """initialized size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
