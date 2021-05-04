#!/usr/bin/python3
def max_integer(my_list=[]):
    if 0 == len(my_list):
        return None
    my_list.sort()
    biggest = my_list[-1]
    return biggest
