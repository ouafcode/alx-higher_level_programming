#!/usr/bin/python3
""" define student class """


class Student():
    """ define student class """
    def __init__(self, first_name, last_name, age):
        """ Initialising a class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ convert to json """
        if isinstance(attrs, list) and all(type(i) == str for i in attrs):
            return ({k: getattr(self, k) for k in attrs if hasattr(self, k)})
        else:
            return (self.__dict__)
