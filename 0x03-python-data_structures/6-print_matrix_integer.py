#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for value in list:
            print("{:d}".format(value), end=' ')
        print()
