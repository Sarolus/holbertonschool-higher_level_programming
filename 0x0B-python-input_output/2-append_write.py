#!/usr/bin/python3

"""
    File - Append Module
"""


def append_write(filename="", text=""):
    """
        Append a string at the end of a text file and
        returns the number of characters added.
    """
    with open(filename, mode="a") as file:
        return file.write(text)
