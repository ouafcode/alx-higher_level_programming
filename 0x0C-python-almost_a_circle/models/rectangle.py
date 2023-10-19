#!/usr/bin/python3
""" Define Rectangle class inherit from base """
from models.base import Base


class Rectangle(Base):
    """ Define Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialise attribute """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        self.id = id

    @property
    def width(self):
        """ to get width value"""
        return self.__width

    @width.setter
    def width(self, width):
        """ to set width value """
        self.__width = width

    @property
    def height(self):
        """ to get height value """
        return self.__height

    @height.setter
    def height(self, width):
        """ to set height value """
        self.__height = height

    @property
    def x(self):
        """ to get x value """
        return self.__x

    @x.setter
    def x(self, x):
        """ to set x value """
        self.__x = x

    @property
    def y(self):
        """ to get y value """
        return self.__y

    @y.setter
    def y(self, y):
        """ to set y value """
        self.__y = y
