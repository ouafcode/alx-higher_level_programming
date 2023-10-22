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
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
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
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value

    def to_dictionary(self):
        """ return dict representatiom of Square """
        return ({'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y})
