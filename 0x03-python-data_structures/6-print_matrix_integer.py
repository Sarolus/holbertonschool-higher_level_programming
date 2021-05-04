#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in range(len(matrix)):
        for column in range(len(matrix[line])):
            print(matrix[line][column], end=" ")
        print()
