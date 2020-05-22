#!/usr/bin/python3
"""print_square module"""


def print_square(size):
    """function that prints a square of size 'size' with '#'"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
