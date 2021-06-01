#!/usr/bin/python3

"""
    Module containing a class prototype that
    inherits from another class called list
    and has a sorted print method.
"""


class MyList(list):
    """
        Class that inherits from List.
    """
    def print_sorted(self):
        """
            Print the list, but sorted (ascending sort).
        """
        print(sorted(self))
