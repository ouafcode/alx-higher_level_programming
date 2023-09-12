#!/usr/bin/python3
""" Funtion writes an Object to a text file, using a JSON """
import json


def save_to_json_file(my_obj, filename):
    """ Funtion writes an Object to a text file, using a JSON """
    with open(filename, 'w') as f:
        return f.write(json.dumps(my_obj))
