#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or len(my_list) == 0:
        return 0

    weighted_sum = weights = 0
    for tup in my_list:
        weighted_sum += tup[0] * tup[1]
        weights += tup[1]
    return weighted_sum / weights
