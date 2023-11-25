#!/usr/bin/python3
def add_integer(a, b=98):
    """ function to add two integers.
    Args:
        a (int) : the input number
        b (int) : the input number

    Returns:
        int : the sum of two input

    Raises:
        TypeError : if the input number is not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
