#!/usr/bin/python3
""" function to append str at the end of text file """


def append_write(filename="", text=""):
    """ function to append str at the end of text file """
    with open(filename, 'a') as f:
        return f.write(text)
