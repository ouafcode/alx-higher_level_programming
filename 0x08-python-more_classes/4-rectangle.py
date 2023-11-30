#!/usr/bin/python3
""" define Rectangle Class """


class Rectangle():
    """ define Rectangle class """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ Private instance attribute width """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ Private instance attribute height """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ define rectangle area """
        return (self.width * self.height)

    def perimeter(self):
        """ define rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return (0)
        else:
            return ((self.width + self.height) * 2)

    """ print the rectangle with the character # """
    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ("")
        return ((("#" * self.width) + "\n") * self.height)[:-1]

    """ return strinf representation of Rectangle """
    def __repr__(self):
        return("Rectangle (" + str(self.width) + "," + " "
                             + str(self.height) + ")")
