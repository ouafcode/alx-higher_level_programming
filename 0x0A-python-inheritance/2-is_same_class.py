#!/usr/bin/python3
""" Return true if the object is exactly an instance """


def is_same_class(obj, a_class):
    """
    Return true if the object an  instance of a the specified class
    """
    return type(obj) == a_class
