#!/usr/bin/python3

"""
    MyInt Module
"""


class MyInt(int):
    """
        Rebel class, wouhou !
    """
    def __eq__(self, other):
        """
            Change behavior of == to !=
        """
        return int(self) != other

    def __ne__(self, other):
        """
            Change behavior of != to ==
        """
        return int(self) == other
