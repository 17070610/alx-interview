#!/usr/bin/python3
"""Module for rotating a 2d matrix"""


def rotate_2d_matrix(matrix):
    """Rotates the matrix"""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
