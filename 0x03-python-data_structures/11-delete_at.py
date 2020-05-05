#!/usr/bin/python3
def delete_at(list=[], idx=0):
    if list == []:
        return list
    if idx < 0:
        return list
    if idx >= len(list):
        return list
    else:
        del list[idx]
        return list
