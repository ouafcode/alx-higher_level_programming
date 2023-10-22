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

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string """
        new = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            new = json.loads(json_string)
        return (new)

    @classmethod
    def create(cls, **dictionary):
        """  returns an instance with all updated attribute """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        loader = []
        dicts = []
        file_name = cls.__name__+'.json'
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                strg = f.read()
                dicts = cls.from_json_string(strg)
                for x in dicts:
                    loader.append(cls.create(**x))
        return loader
