#!/usr/bin/python3
def max_integer(my_list=[]):
    max_v = my_list[0]
    for i in range(len(my_list) - 1):
        if max_v >= my_list[i + 1]:
            max_v = max_v
        else:
            max_v = my_list[i + 1]
    return max_v
