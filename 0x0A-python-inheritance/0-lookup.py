#!/usr/bin/python3
""" Creating a function Lookup"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    """
    return dir(obj)
