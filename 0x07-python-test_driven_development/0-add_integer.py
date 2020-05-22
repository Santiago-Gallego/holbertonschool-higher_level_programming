#!/usr/bin/python3
"""
 Return the sum of a and b
 This function edits floats to integers
 This will raise errors
"""


def add_integer(a, b=98):
    """
     Add two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
