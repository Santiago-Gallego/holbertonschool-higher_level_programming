#!/usr/bin/python3
""" Writes an Object to a text file """
import json


def save_to_json_file(my_obj, filename):
    """ save JSON file """
    with open(filename, 'w') as f:
        json.dumps(my_obj,f)
