#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for sum_ in set(my_list):
        add += sum_
    return add
