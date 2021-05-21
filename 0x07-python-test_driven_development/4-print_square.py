#!/usr/bin/python3

"""
Function that prints a square with the character #
"""


def print_square(size):

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for cell in range(size):
        print("{}".format("#" * size))
