#!/usr/bin/python3
""" define class MyInt that inherits from int """

class MyInt(int):
    """ define class MyInt that inherits from int """
    def __init__(self, value):
        self.value = value

    def __eq__(self, value):
        return False

    def __ne__(self, value):
        return True
