#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score = sum(nb[0] * nb[1] for nb in my_list)
    weight = sum(nb[-1] for nb in my_list)
    return score/weight
