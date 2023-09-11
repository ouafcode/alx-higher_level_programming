#!/usr/bin/python3
""" sub of class """


def inherits_from(obj, a_class):
    """
    Return true if the object an instance of a class
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
