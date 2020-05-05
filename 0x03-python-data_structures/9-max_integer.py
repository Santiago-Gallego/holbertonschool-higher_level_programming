#!/usr/bin/python3
def max_integer(list=[]):
    if len(list) == 0:
        return None
    max_val = list[0]
    for i in list:
        if i > max_val:
            max_val = i
    return max_val
