#!/usr/bin/python3
""" function to creates an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """ create object from json file """
    with open(filename, 'w') as f:
        return (json.load(f))
