#!/usr/bin/python3
def replace_in_list(list, idx, element):
    if list == []:
        return list
    if idx < 0:
        return list
    if idx >= len(list):
        return list
    else:
        list[idx] = element
        return list
