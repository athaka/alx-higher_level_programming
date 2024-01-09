#!/usr/bin/python3
# Author: Jonathan Esokawu


def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j != (len(matrix[i]) - 1):
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]))
