#!/usr/bin/python3
""" Create class for defining square """


class Square:
    """ Create class for defining square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialising attribute instance
        Args: size: size of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Getting the size of square """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting the size of square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ get the position """
        return self.__position

    @position.setter
    def position(self, value):
        """ set position to value """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ return current square area """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.__size == 0:
            print()
            return
        for x in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for y in range(0, self.__position[0]):
                print(" ", end='')
            for j in range(0, self.__size):
                print("#", end='')
            print()
