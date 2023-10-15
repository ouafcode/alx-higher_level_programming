#!/usr/bin/python3
"""  function that returns the dictionary description in Json """
import json


def class_to_json(obj):
    """  function that returns the dictionary description in Json """
    return (obj.__dict__)
