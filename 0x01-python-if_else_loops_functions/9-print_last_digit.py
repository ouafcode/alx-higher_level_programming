#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lst = ((-1 * number) % 10)
    else:
        lst = number % 10
    print("{}".format(lst), end="")
    return lst
