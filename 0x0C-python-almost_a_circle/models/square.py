#!/usr/bin/python3
""" Define Square class inherit from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialisation of attribute """
        self.size = size
        width = height = size
        super().__init__(width, height, x, y, id)

    def __str__(self):
        """ Define str representation """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.size))
