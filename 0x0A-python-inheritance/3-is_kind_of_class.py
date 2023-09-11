#!/usr/bin/python3
""" Function return true if the object an instance """


def is_kind_of_class(obj, a_class):
    """
    Return true if the object an instance or false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
