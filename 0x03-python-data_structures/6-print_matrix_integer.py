#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        for val in row:
            r_len = len(row)
            i += 1
            print("{:d}".format(val), end='')
            if i != r_len:
                print(" ", end='')
        print('')
