#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
        return (True)
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=stderr)
        return (False)
