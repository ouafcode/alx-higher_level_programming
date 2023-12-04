#!/usr/bin/python3
""" define MyInt ingerits from int """


class MyInt(int):
    """ define MyInt ingerits from int """
    def __ne__(self, other):
        return (True)

    def __eq__(self, other):
        return (False)
