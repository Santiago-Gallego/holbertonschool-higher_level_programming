#!/usr/bin/python3
"""
Read N Lines
"""


def read_lines(filename="", nb_lines=0):
    """ Read n lines of text file """
    line_count = 0
    with open(filename, 'r') as f:
        if number_lines <= 0:
            print(f.read(), end='')
        for line in f:
            if line_count < number_lines:
                print(line, end='')
                line_count += 1
