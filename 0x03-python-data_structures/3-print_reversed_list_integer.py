#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if 0 == len(my_list):
        return None
    for n in reversed(my_list):
        print("{:d}".format(n))
