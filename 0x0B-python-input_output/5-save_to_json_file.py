#!/usr/bin/python3
""" Encoding object to json in file """
import json


def save_to_json_file(my_obj, filename):
    """ Encoding object to json in file """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
