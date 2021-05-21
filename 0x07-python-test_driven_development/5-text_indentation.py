#!/usr/bin/python3

"""
Function that prints a text with 2 new lines after each
of these characters : "., ?, :"
"""


def text_indentation(text):
    string = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    inc = 0
    for c in text:
        if inc == 0:
            if c == ' ':
                continue
            else:
                inc = 1
        if inc == 1:
            string += c
        if c in ('.', '?', ':'):
            string += "\n\n"
            inc = 0
    print(string, end='')
