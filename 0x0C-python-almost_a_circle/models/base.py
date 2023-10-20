#!/usr/bin/python3
""" Define the base class of project """
import json
import csv
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """ write json string of object in to file """
        if list_objs is None or list_objs == []:
            ljson = "[]"
        else:
            ljson = cls.to_json_string([x.to_dictionary() for x in list_objs])

        name_file = cls.__name__+".json"
        with open(name_file, 'w') as f:
            f.write(ljson)
