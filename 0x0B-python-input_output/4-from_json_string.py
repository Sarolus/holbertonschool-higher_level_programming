#!/usr/bin/python3

"""
    File - JSON Module
"""
import json


def from_json_string(my_str):
    """
        Return an object (Python data structure)
        representend by a JSON string.
    """
    return json.loads(my_str)
