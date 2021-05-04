#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in range(len(matrix)):
        for column in range(len(matrix[line])):
            print("{:d}".format(matrix[line][column]), end='')
            if column < (len(matrix[line]) - 1):
                print(" ", end='')
        print()
