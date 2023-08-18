#!/usr/bin/python3
def uniq_add(my_list=[]):
    sums = 0
    for x in set(my_list):
        sums = sums + x
    return (sums)
