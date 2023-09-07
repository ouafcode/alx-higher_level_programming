#!/usr/bin/python3
""" Create a rectangle class """


class Rectangle:
    """ Class that defines a rectangle """
    def __init__(self, width=0, height=0):
        """ to inisialize n object for instance """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return rectangle area """
        return self.width * self.height

    def perimeter(self):
        """ return rectangle perimeter """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.height + self.width) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ('')
        else:
            return ((('#' * self.width) + "\n") * self.height)[:-1]

    def __repr__(self):
        return ("Rectangle(" + str(self.width) + "," + " " +
                str(self.height) + ")")

    def __del__(self):
        print("Bye rectangle...")
