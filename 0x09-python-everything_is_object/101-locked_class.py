#!/usr/bin/python3
"""  prevents user to create new instance """


class LockedClass:
    """ prevents user to create new instance """
    __slots__ = ['first_name']
