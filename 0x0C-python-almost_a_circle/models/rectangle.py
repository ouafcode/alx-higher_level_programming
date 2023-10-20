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

    @property
    def width(self):
        """ to get width value"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ to get height value """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ to get x value """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ to get y value """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ calcul area of rectangle """
        return (self.__width * self.__height)

    def display(self):
        """ display the character # """
        print(("\n" * self.y)+((" " * self.x)+("#" * self.width) + "\n")
              * self.height, end="")

    def __str__(self):
        return ("[Rectangle] (" + str(self.id) + ") " + str(self.x) + "/" +
                str(self.y) + " - " + str(self.width) + "/" + str(self.height))

    def update(self, *args, **kwargs):
        """ update class Rectangle attribut """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "width":
                    self.width = value
                elif key == "id":
                    self.id = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ return dict representation of class """
        return ({'x': self.x, 'y': self.y, 'height': self.height, 'width': self.width})
