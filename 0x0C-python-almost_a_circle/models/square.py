#!/usr/bin/python3
""" this is modele square """

from models.rectangle import Rectangle


def validate_integers(n, v):
    """ check if is a valid integer """
    list_ = ['width', 'height', 'x', 'y']
    if type(v) != int:
        raise TypeError("{} must be an integer".format(n))
    if (n == list_[0] or n == list_[1]) and v <= 0:
        raise ValueError("{} must be > 0".format(n))
    if (n == list_[2] or n == list_[3]) and v < 0:
        raise ValueError("{} must be >= 0".format(n))


class Square(Rectangle):
    """ The class Saquare """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """ Getter and Setter """
    @property
    def size(self):
        """get size."""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        validate_integers('width', value)
        self.width = value
        self.height = value

    def __str__(self):
        """ String representation """
        return ('[Square] ({}) {}/{} - {}'.format(self.id,
                self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ assign the positions to the list """
        if args:
            list_ = ['id', 'size', 'x', 'y']
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
                if key.endswith('width') or key.endswith('height'):
                    new_key = 'size'
                new_dicc[new_key] = dicc[key]
            return new_dicc
