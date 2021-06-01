#!/usr/bin/python3
"""
    Module containing add_attribute function.
"""


def add_attribute(obj, name, value):
    """
        Adds a new attribute to the given object
        if it's possible
    """
    if not hasattr(obj, name):
        raise TypeError("can't add new attribute")
    setattr(object, name, value)
