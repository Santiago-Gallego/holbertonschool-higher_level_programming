#!/usr/bin/python3
def print_last_digit(number):
    d = abs(number) % 10
    print("{:d}".format(d), end="")
    return d
