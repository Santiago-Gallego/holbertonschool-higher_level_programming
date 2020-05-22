#!/usr/bin/python3
"""matrix_divided module"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""

    def check_samesize_lists_in_matrix(matrix):
        """checks if lists in matrix are same size"""
        size = len(matrix[0])
        for i in range(1, len(matrix)):
            if len(matrix[i]) != size:
                return False
        return True

    def is_list_of_lists_of_intfloats(matrix):
        """checks if matrix is a list of lists of ints and floats"""
        if matrix is None:
            return False
        for row in matrix:
            if type(row) is not list:
                return False
            for i in row:
                if type(i) is not int and type(i) is not float:
                    return False
        return True

    if matrix == [[]] or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if is_list_of_lists_of_intfloats(matrix) is False:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if check_samesize_lists_in_matrix(matrix) is False:
        raise TypeError("Each row of the matrix must have the same size")
    if div is None or (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i/div, 2) for i in row] for row in matrix]
