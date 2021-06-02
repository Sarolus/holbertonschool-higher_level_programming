#!/usr/bin/python3

"""
    File - JSON Module
"""
import json


def load_from_json_file(filename):
    """
        Create an object from a "JSON file".
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
