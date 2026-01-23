#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    return [[num ** 2 for num in row] for row in matrix]
