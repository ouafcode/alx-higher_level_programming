#!/usr/bin/python3
""" function that reads a text file (UTF8) """


def read_file(filename=""):
    """ function that reads a text file (UTF8) """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
