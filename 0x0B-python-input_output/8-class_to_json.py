#!/usr/bin/python3

"""
    Class to JSON object Module
"""


def class_to_json(obj):
    """
        Return the dictionary description with simple data
        structure (list, dictionary, string, integer and
        boolean) for JSON serialization of an object.
    """
    return getattr(obj, "__dict__")
