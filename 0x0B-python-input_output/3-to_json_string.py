#!/usr/bin/python3
""" function return JSON representation of an object (string) """

import json


def to_json_string(my_obj):
    """ function return JSON representation of an object (string) """
    return json.dumps(my_obj)
