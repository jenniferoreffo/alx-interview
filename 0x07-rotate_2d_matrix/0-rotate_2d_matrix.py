#!/usr/bin/python3


""" module to rotate a 2D matrix """


def rotate_2d_matrix(matrix):
    """
    rotate_2d_matrix
    Args:
        matrix
    Return:
        Nothing
    """
    n = len(matrix)

    "Transposing the matrix"
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    "Reverse each row"
    for i in range(n):
        matrix[i] = matrix[i][::-1]

