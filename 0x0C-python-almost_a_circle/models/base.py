#!/usr/bin/python3
""" Define Base class """
import json
import os
import csv


class Base():
    """ Define Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return Json string """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        if (type(list_dictionaries) != list or not all(type(x) == dict
           for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ to write json string to file """
        files = cls.__name__ + ".json"
        if list_objs is None:
            ljson = "[]"
        else:
            ljson = cls.to_json_string([x.to_dictionary() for x in list_objs])
        with open(files, "w") as f:
            f.write(ljson)

    @staticmethod
    def from_json_string(json_string):
        """ return list of json representation """
        new = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            new = json.loads(json_string)
        return (new)

    @classmethod
    def create(cls, **dictionary):
        """ return instance using dummy """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """ return a list of instances """
        loader = []
        dicts = []
        files = cls.__name__ + ".json"
        if os.path.exists(files):
            with open(files, 'r') as f:
                str_r = f.read()
                dicts = cls.from_json_string(str_r)
            for x in dicts:
                loader.append(cls.create(**x))
        return (loader)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to csv file """
        if(type(list_objs) != list and
           list_objs is not None or
           not all(isinstance(i, cls) for i in list_objs)):
            raise TypeError("list_objs must be a list of instance")
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is not None:
                list_dict = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fields)

                writer.writeheader()
                writer.writerows(list_dict)

    @classmethod
    def load_from_file_csv(cls):
        """ load from csv file """
        loader = []
        filename = cls.__name__ + ".csv"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                csv_read = csv.reader(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    field = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    field = ['id', 'size', 'x', 'y']
                for i, row in enumerate(csv_read):
                    if i > 0:
                        x = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(x, field[j], int(e))
                        loader.append(x)
        return (loader)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """to opens a window and draws all the instances"""

        import turtle
        import time
        from random import randrange

        p = turtle.Turtle()
        p.color("light green")
        turtle.bgcolor("violet")
        p.shape("square")
        p.pensize(8)

        for x in (list_rectangles + list_squares):
            p.penup()
            p.setpos(0, 0)
            turtle.Screen().colormode(255)
            p.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_open(p, x)
            time.sleep(1)
        time.sleep(5)

    @staticmethod
    def draw_open(p, rect):
        """ draws a Rectangle or Square."""

        p.penup()
        p.setpos(rect.x, rect.y)
        p.pendown()
        p.forward(rect.width)
        p.left(90)
        p.forward(rect.height)
        p.left(90)
        p.forward(rect.width)
        p.left(90)
