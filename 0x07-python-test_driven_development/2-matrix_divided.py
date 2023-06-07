#!/usr/bin/python3
""" Matrix divided module"""

def matrix_divided(matrix, div):
    """ Takes in a matrix and divider and divides all elements."""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size = len(matrix[0])
    for arr in matrix:
        if not isinstance(arr, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(arr) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for element in arr:
            if not isinstance(element, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result_array = []
    for arr in matrix:
        result_array.append(list(map(lambda x: round(x / div, 2), arr)))
    return result_array
