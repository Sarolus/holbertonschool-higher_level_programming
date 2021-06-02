#!/usr/bin/python3

"""
    Search and Update Module
"""


def append_after(filename="", search_string="", new_string=""):
    """
        Insert a new line to a file, after each line
        containing a specific string.
    """
    new_line = ""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            new_line += line
            if search_string in line:
                new_line += new_string

    with open(filename, mode="w") as file:
        file.write(new_line)
