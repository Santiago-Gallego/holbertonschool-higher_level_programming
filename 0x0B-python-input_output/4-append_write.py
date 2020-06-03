#!/usr/bin/python3
""" Append values to a file """


def append_write(filename="", text=""):
    """ Appends string to the end text file """
    with open(filename, 'a') as f:
        return f.write(text)
