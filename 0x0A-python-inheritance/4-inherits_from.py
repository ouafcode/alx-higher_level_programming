#!/usr/bin/python3
""" check if the object is an instance
of a class that inherited """


def inherits_from(obj, a_class):
    """ to check subclass """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return (True)
    else:
        return (False)
