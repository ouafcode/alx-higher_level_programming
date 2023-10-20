#!/usr/bin/python3
""" Define Square class inherit from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialisation of attribute """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Define str representation """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))

    @property
    def size(self):
        """ get the size of square """
        return self.width

    @size.setter
    def size(self, value):
        """ set the size of square """
        self.width = value
        self.height = value
