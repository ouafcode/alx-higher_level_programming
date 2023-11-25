#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """ funtion that prints My name is <first name> <last name>
    Args:
        first name (str) : input first name
        last name (str) : input last name
    Return:
        string My name is <first name> <last name>
    Raise:
        TypeError: first_name must be a string or last_name must be a string
    """

    if not isinstance(first_name, str) or first_name == "":
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
