#!/usr/bin/python3
""" Define the base class of project """
import json


class Base():
    """ define class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Intialisation of class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
