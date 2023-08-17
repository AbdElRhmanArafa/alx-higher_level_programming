#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for row in matrix:
        tempList = list(map(lambda x: x ** 2, row))
        newMatrix.append(tempList)
    return newMatrix
