#!/usr/bin/python3
""" Create a rectangle class """


class Rectangle:
    """ Class that defines a rectangle """
    def __int__(self, width=0, height=0):
        """ to inisialize n object for instance """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ to retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ to set width to value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ to retreive height """
        return self.__height

    @height.setter
    def height(self, value):
        """ to ste height to value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
