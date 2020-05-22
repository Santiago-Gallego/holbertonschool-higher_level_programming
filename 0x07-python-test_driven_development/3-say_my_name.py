#!/usr/bin/python3
"""say_my_name module"""


def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name> first_name is required"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    name = 'My name is ' + first_name + ' ' + last_name
    print(name)
