#!/usr/bin/python3
""" adds a new attribute to an object """


def add_attribute(obj, new_attr, value):
    """ add attribute """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, new_attr, value)
