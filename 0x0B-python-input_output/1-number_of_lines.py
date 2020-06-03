#!/usr/bin/python3
""" Number of Lines """


def number_of_lines(filename=""):
    """ Number of Lines """
    linecount = 0
    with open(filename, 'r') as f:
        for line in f:
            linecount += 1
    return linecount
