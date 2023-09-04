#!/usr/bin/python3
""" Create class for defining square """


class Square:
    """ Create class for defining square """
    def __init__(self, size=0):
        """ Initialising attribute instance
        Args: size: size of square
        """
        self.size = size

    @property
    def size(self):
        """ Getting the size of square """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting the size of square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return current square area """
        return self.__size ** 2
