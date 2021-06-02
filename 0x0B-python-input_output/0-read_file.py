#!/usr/bin/python3

"""
    File - Read Module
"""


def read_file(filename=""):
    """
        Read a text file and prints it to stdout.
    """
    if isinstance(filename, str):
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read(), end='')
