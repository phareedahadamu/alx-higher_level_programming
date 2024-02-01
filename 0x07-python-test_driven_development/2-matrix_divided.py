#!/usr/bin/python3
""" A function that divides all elements of a matrix.
- Returns a new matrix"""


def matrix_divided(matrix, div):
    """matrix must be a list of lists of integers or floats
- Each row of the matrix must be of the same size
- div must be a number (integer or float)
- div can’t be equal to 0
- All elements of the matrix should be divided by div, rounded to 2
decimal places"""
    if not (all(all(isinstance(item, int) for item in row) for row in matrix)
            or all(all(isinstance(item, float) for item in row)
            for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not (all(len(sublist) == len(matrix[0]) for sublist in matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []
    i = 0
    while i < len(matrix):
        tmp = []
        for j in matrix[i]:
            tmp.append(round((j/div), 2))
        new_list.append(tmp)
        i += 1
    return new_list
