#!/usr/bin/python3
"""Simple Rectangle Class"""


class Rectangle:
    """ Class - empty """

    def __init__(self, width=0, height=0):
        """ width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ method to find the area """
        return self.__height * self.__width

    def perimeter(self):
        """ method to find the perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """ representation square """
        stri = ""
        if self.__height == 0 or self.__width == 0:
            return stri
        for y in range(self.__height):
            for x in range(self.__width):
                stri += "#"
            stri += "\n"
        stri = stri[:-1]
        return stri

    def __repr__(self):
        """ reresentation square instance """
        w = str(self.__width)
        h = str(self.__height)
        return "Rectangle(" + w + ", " + h + ")"

    def __del__(self):
        """ messsage for deletion """
        print("Bye rectangle...")
