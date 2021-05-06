#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    return [replace if bool == search else bool for bool in my_list]
