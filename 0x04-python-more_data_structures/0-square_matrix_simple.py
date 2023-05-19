#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res_matrix = []
    for i in matrix:
        row = []
        for j in i:
            row.append(j * j)
        res_matrix.append(row)
    return res_matrix
