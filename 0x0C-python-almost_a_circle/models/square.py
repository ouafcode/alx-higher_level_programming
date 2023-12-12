#!/usr/bin/python3
""" Define Square class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define Square class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get the size """
        return self.width

    @size.setter
    def size(self, value):
        """ set the size """
        self.width = value
        self.height = value

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ update attribute """
        if args:
            for i in range(len(args)):
                if i == 0:
                    if type(args[0]) != int and args[0] is not None:
                        raise TypeError("id must be an integer")
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.x = args[2]
                elif i == 3:
                    self.y = args[3]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ return dictionnary representation """
        return ({'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y})
