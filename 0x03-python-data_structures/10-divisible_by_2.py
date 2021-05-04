#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool = []
    for n in my_list:
        if 0 == n % 2:
            bool.append(True)
        else:
            bool.append(False)

    return bool
