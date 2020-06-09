#!/usr/bin/python3
""" this is the module rectangule """

from models.base import Base


def validate_integers(n, v):
    """ check if is a valid integer """
    list_ = ['width', 'height', 'x', 'y']
    if type(v) != int:
        raise TypeError("{} must be an integer".format(n))
    if (n == list_[0] or n == list_[1]) and v <= 0:
        raise ValueError("{} must be > 0".format(n))
    if (n == list_[2] or n == list_[3]) and v < 0:
        raise ValueError("{} must be >= 0".format(n))


class Rectangle(Base):
    """ Rectangle class extends from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize the attributes """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ Getters and Setters """
    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        validate_integers('width', value)
        self.__width = value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        validate_integers('height', value)
        self.__height = value

    @property
    def x(self):
        """ get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x """
        validate_integers('x', value)
        self.__x = value

    @property
    def y(self):
        """ get y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set y """
        validate_integers('y', value)
        self.__y = value

    """ Funcition area """
    def area(self):
        """ return area """
        return self.__width * self.__height

    """ Function display figure """
    def display(self):
        """ Draw figure """
        if (self.area() == 0):
            print('')
            return
        for move_y in range(0, self.__y):
            print('')
        for height in range(0, self.__height):
            for move_x in range(0, self.__x):
                print(' ', end='')
            for width in range(0, self.__width):
                print('#', end='')
            print('')

    """ Function return string representation """
    def __str__(self):
        """ write representation """
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    """
    Function overwrite attribute values
    to each attribute
    """
    def update(self, *args, **kwargs):
        """ assign the positions to the list """
        if args:
            list_ = ['id', 'width', 'height', 'x', 'y']
            for index, value in enumerate(args):
                setattr(self, list_[index], value)
            return
        for key in kwargs:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """return dict of the instance"""
        dicc = self.__dict__
        new_dicc = {}
        new_key = ''
        if dicc:
            for key in dicc:
                new_key = key
                if key.startswith('_'):
                    new_key = key[12:]
                new_dicc[new_key] = dicc[key]
            return new_dicc
