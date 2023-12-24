#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    tmp = []
    k = 0
    for i in matrix:
        matrix2.append(list(map(lambda x, y : x * y, i, i)))
    return matrix2
