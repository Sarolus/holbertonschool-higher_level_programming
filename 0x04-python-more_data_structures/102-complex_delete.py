#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for itemKey, itemValue in list(a_dictionary.items()):
        if itemValue == value:
            del a_dictionary[itemKey]
    return a_dictionary
