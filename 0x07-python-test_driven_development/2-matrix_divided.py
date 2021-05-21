#!/usr/bin/python3

"""
Function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    new_matrix = []
    matrix_err = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for y in matrix:
        row = []
        if not isinstance(y, list):
            raise TypeError(matrix_err)
        length = len(matrix[0])
        if length != len(y):
            raise TypeError("Each row of the matrix must have the same size")
        for x in y:
            if not isinstance(x, (int, float)):
                raise TypeError(matrix_err)
            result = round(float(x / div), 2)
            row.append(result)
        new_matrix.append(row)

    return new_matrix
