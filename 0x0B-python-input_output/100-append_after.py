#!/usr/bin/python3
"""inserts a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text"""
    with open(filename, 'r') as f:
        rline = f.readlines()
    with open(filename, 'w') as f:
        for rline in lines:
            if search_string in rline:
                f.write(rline + new_string)
            else:
                f.write(rline)
