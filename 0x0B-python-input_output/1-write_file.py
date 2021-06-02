#!/usr/bin/python3

"""
    File - Write Module
"""


def write_file(filename="", text=""):
    """
        Write a string to a text file and
        returns the number of characters written.
    """
    with open(filename, mode="w") as file:
        return file.write(text)
