#!/usr/bin/python3
""" to check subclass """


def inherits_from(obj, a_class):
    """ to check subclass """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return (True)
    else:
        return (False)
