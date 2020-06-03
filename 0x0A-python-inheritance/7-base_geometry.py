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
