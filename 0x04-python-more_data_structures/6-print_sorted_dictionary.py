#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for entry in sorted(a_dictionary.keys()):
        print("{}: {}".format(entry, a_dictionary[entry]))
