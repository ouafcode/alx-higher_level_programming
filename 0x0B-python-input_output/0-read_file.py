#!/usr/bin/python3
""" function that reads a text file (UTF8) """


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        rfile = f.read()
        print(rfile)
