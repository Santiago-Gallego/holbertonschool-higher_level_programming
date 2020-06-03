#!/usr/bin/python3
""" Write to a File """


def write_file(filename="", text=""):
    """ writing file """
    with open(filename, mode='w') as f:
        return f.write(text)
