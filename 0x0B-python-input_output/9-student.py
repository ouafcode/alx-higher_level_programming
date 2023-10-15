#!/usr/bin/python3
""" define student class """


class Student():
    """ define student class """
    def __init__(self, first_name, last_name, age):
        """ Initialising a class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ convert to json """
        return (self.__dict__)
