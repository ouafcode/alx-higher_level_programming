#!/usr/bin/python3
""" class BaseGeometry """


class BaseGeometry():
    """ define class baseGeometry """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(self.value, int):
            raise TypeError("{} must be an integer".format(self.value))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.value))
