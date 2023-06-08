#!/usr/bin/python3
"""a function that rotate an n x n 2D matrix to 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """Rotate an n x n 2D matrix by 90 degrees clockwise"""
    matrix.reverse()  # reverse the matrix
    length = len(matrix)  # length of the matrix
    matrix_copy = matrix.copy()  # copy the matrix

    for col in range(length):
        matrix[col] = [row[col] for row in matrix_copy]
