#!/usr/bin/python3
def print_square(size):
    """  function to prints a square with the character #.
    Args:
        size (int) : size length of the square
    Return:
        square with character #
    Raise:
        ValueError: if size is less than 0
        TypeError: if size is a float and is less than 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
