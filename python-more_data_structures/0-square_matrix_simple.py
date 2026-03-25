#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row[]:
            new_row.append(item ** 2)
    return new_matrix
