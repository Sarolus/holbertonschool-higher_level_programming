#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx in my_list:
        my_list.remove(idx + 1)
        return my_list
    return my_list
