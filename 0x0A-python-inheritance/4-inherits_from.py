#!/usr/bin/python3
""" function return true if the object is a instance from class inheritance """


def inherits_from(obj, a_class):
    """ Return True or false """
    if(type(obj) == a_class):
        return False
    return isinstance(obj, a_class)
