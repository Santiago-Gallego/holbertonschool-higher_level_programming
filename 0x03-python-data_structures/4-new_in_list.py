#!/usr/bin/python3
def new_in_list(list, idx, element):
    if idx < 0:
        return list
    if idx >= len(list):
        return list
    else:
        new_list = list.copy()
        new_list[idx] = element
        return new_list
