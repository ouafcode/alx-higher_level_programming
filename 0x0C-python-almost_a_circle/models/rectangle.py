#!/usr/bin/python3
""" Define Rectangle class inherit from base """
from base import Base


class Rectangle(Base):
    """ Define Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialise attribute """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(self, id)

    """ getter and setter function for width """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    """ getter and setter function for height """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, width):
        self.__height = height

    """ getter and setter for x """
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    """ getter and setter for y """
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
