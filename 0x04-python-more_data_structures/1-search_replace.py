#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if bool == search else bool for bool in my_list]
