#!/usr/bin/python3
""" define MyInt ingerits from int """


class MyInt(int):
    def __ne__(self, other):
        return (True)

    def __eq__(self, other):
        return (False)
