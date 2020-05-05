#!/usr/bin/python3
def divisible_by_2(list=[]):
    list_2 = list.copy()
    for i in range(len(list_2)):
        if list[i] % 2 == 0:
            list_2[i] = True
        else:
            list_2[i] = False
    return list_2
