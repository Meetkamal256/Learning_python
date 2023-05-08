#!/usr/bin/python3
""" 
this module has one function that divides all element of a matrix
"""


def matrix_divided(matrix, div):
    if not isinstance(matrix, int) and not isinstance(matrix, float):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
