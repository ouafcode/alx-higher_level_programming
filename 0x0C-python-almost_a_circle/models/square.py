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

    def update(self, *args, **kwargs):
        """ update attribute of class square """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = self.height =  args[1]
                elif i == 2:
                    self.x = args[2]
                elif i == 3:
                    self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.width = self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                elif key == "id":
                    self.id = value
