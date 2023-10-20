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
        if (type(list_objs) != list and list_objs is not None
           or not all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be list of objects")

        name_file = cls.__name__+".csv"
        with open(name_file, 'w') as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)
