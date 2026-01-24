#!/usr/bin/python3
"""
Module for matrix_divided function.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix: list of lists of integers or floats
        div: number (integer or float) to divide by

    Returns:
        new matrix with divided elements rounded to 2 decimal places

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats
        TypeError: if each row of the matrix is not of the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is equal to 0
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or not matrix:
        raise TypeError(msg_type)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg_type)
        if len(row) != len(matrix[0]):
            raise TypeError(msg_size)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg_type)

    return [[round(x / div, 2) for x in row] for row in matrix]
