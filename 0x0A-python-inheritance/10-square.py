#!/usr/bin/python3
""" Geometry Class """


class BaseGeometry:
    """ arithmetic operations """
    def area(self):
        """ area calculation """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate integers """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

""" class rectangle """



class Rectangle(BaseGeometry):
    """ rectangle class """
    def __init__(self,width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """ representation string """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

""" class square """


class Square(Rectangle):
    """ square class """
    def __init__(self,size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
