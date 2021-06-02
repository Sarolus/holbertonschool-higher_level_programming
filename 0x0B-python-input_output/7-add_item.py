#!/usr/bin/python3

"""
    File - Load, Add, Save Module
"""
from sys import argv
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(prmFilename, prmArgc):
    """
        Adds all arguments to a Python list,
        and then save them to a file
    """
    try:
        my_list = load_from_json_file(filename)
    except:
        my_list = []

    for i in range(1, argc):
        my_list.append(argv[i])
    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    argc = len(argv)
    filename = "add_item.json"
    add_item(filename, argc)
