#!/usr/bin/python3
def no_c(my_string):
    temp = list(my_string)
    for i in temp:
        if i == "c" or i == "C":
            temp.remove(i)
    return ("".join(temp))
