#!/usr/bin/python3
"""
2-matrix_divided module.

This module provides a function that divides all elements of a matrix by a divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Parameters:
        matrix (list of lists): Matrix of integers/floats.
        div (int|float): Divisor.

    Returns:
        list of lists: New matrix with all values divided by div.

    Raises:
        TypeError: If matrix is not a matrix (list of lists) of integers/floats.
        TypeError: If each row of matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = None

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_matrix.append([round(element / div, 2) for element in row])

    return new_matrix
