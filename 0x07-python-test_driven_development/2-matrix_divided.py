#!/usr/bin/python3
"""
Module containing one function that divides all
elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix

    Args:
        matrix: list of lists of integers or floats
        div: number by which elements of matrix are divided

    Return:
        New matrix containg elements in matrix divided by div

    Raises:
        TypeError if an element in matrix is not integer or float
        TypeError if rows in matrix have different sizes
        TypeError if div is not an integer or float
        ZeroDivisionError if div is 0
    """

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    len_row = len(matrix[0])
    for row in matrix:
        if len_row != len(row):
            raise TypeError("Each row of the matrix must have the same size")
    new_mat = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            new_mat[i][j] = round(matrix[i][j]/div, 2)
    return new_mat
