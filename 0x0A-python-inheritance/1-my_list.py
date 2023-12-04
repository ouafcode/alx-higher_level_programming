#!/usr/bin/python3
""" prints listed sorted """

class MyList(list):
    """ prints the list sorted """
    def print_sorted(self):
        print(sorted(self))
