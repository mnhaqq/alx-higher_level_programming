#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_mat[i][j] = matrix[i][j] ** 2
    return new_mat
