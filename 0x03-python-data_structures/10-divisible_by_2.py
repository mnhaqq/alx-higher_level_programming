#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    if not my_list:
        return new
    for i in range(len(my_list)):
        if i % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return new
