#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """ Pascal Triangle representation """
    repTriangle = []
    if n <= 0:
        return []
    for line in range(1, n + 1):
        tmp = []
        c = 1
        for i in range(1, line + 1):
            tmp.append(str(c))
            c = c * (line - i) // i
        repTriangle.append(tmp)
    return repTriangle
