#!/usr/bin/python3
"""
    Module containing lookup function
"""


def lookup(obj):
    """
        Return the list of a available attributes and
        methods of an object
    """
    return dir(obj)
