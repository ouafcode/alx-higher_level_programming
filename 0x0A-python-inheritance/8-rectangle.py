#!/usr/bin/python3
""" define class BaseGeometry """


class BaseGeometry():
    """ define class BaseGeometry """
    def area(self):
        """ area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ define class Rectangle """
    def __init__(self, width, height):
        """ instantiation with width and height """
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
