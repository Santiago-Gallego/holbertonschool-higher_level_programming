#!/usr/bin/python3
"""
Return a list of lists of integers representing
the pascal's triangle
"""


def pascal_triangle(n):
    """ Makes a List of lists of integers repr
    the Pascal's Triangle """
    myList = []
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    for lines in range(1, n + 1):
        myList2 = []
        c = 1
        for i in range(1, lines + 1):
            myList2.append(str(c))
            c = c * (lines - i) // i
        myList.append(myList2)
    return myList
