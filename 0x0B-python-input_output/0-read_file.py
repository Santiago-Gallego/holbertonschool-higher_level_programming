#!/usr/bin/python3
""" Read Text File """


def read_file(filename=""):
    """ Function read a text file and prints """
    with open(filename, encoding='utf-8') as f:
        print(f.read())
