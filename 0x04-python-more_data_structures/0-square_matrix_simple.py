#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new = [[i[j] ** 2 for j in range(len(i))] for i in matrix]
    return (new)
