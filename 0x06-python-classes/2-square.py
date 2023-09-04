#!/usr/bin/python3
""" Create class for defining square """


class Square:
    """ Create class for defining square """
    def __init__(self, size):
        """ Initialising attribute instance
        Args: size: size of square
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
