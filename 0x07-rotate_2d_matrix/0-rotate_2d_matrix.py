#!/usr/bin/python3
"""
Rotate 2d matrix module
"""


def rotate_2d_matrix(matrix):
    """Rotate 2d matrix
    """
    matrix[:] = list(map(list, zip(*matrix)))
    for mtrx in matrix:
        mtrx.reverse()