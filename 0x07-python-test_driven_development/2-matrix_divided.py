#!/usr/bin/python3
""" Matrix divided module"""

def matrix_divided(matrix, div):
    """ Takes in a matrix and divider and divides all elements.

    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    >>> matrix_divided([["Hello", "Holberton"], [6, 7]], 3)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix_divided([[3, 4, 5], [6, 7]], 3)
    Traceback (most recent call last):
    TypeError: Each row of the matrix must have the same size

    >>> matrix_divided([[3, 4], [6, 7]], "Hello")
    Traceback (most recent call last):
    TypeError: div must be a number

    >>> matrix_divided("Hello", 9)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix_divided([[3, 4], [6, 7]], 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero

    >>> matrix_divided([[3, 4], [6, 7]], -2)
    [[-1.5, -2.0], [-3.0, -3.5]]

    >>> matrix_divided([[2, 3], [4, 5]], float('inf'))
    [[0.0, 0.0], [0.0, 0.0]]

    >>> matrix = [[1, 2, 3]]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0]]
    >>> print(matrix)
    [[1, 2, 3]]

    >>> matrix_divided([[3, 4]])
    Traceback (most recent call last):
    TypeError: matrix_divided() missing 1 required positional argument: 'div'

    >>> matrix_divided()
    Traceback (most recent call last):
    TypeError: matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'
    """
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
