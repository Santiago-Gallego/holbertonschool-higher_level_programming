#!/usr/bin/python3
def uniq_add(my_list=[]):
    no = list(set(my_list))
    res = 0
    for i in range(len(no)):
        res += no[i]
    return res
