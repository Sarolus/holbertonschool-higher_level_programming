#!/usr/bin/python3

"""
    Locked class module
"""


class LockedClass():
    """
        This is a class that prevents the
        user from dynamically creating new
        instance attributes, except if the
        new instance is called first_name
    """
    __slots__ = "first_name"
