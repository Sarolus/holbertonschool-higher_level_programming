#!/usr/bin/python3

"""
    File - JSON Module
"""
import json


def save_to_json_file(my_obj, filename):
    """
        Write an object to a text file, using
        a JSON representation.
    """
    with open(filename, mode="w") as file:
        json.dump((my_obj), file)
