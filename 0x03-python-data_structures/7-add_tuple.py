#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        for i in range(len(tuple_a), 2):
            tuple_a.append(0)
    if len(tuple_b) < 2:
        for i in range(len(tuple_b), 2):
            tuple_b.append(0)
    list_r = [tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]]
    return tuple(list_r)
