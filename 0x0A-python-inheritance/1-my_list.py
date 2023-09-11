#!/usr/bin/python3
""" Creating class Mylist """


class MyList(list):
    """
    MyList class that inherits from list
    """
    def print_sorted(self):
        """
        to print list sorted
        """
        print(sorted(self))
