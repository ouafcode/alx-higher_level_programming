#!/usr/bin/python3
""" Function that writes str to a text file """


def write_file(filename="", text=""):
    """ Function that writes str to a text file """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
