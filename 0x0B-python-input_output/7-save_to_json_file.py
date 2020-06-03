#!/usr/bin/python3
"""Save Object """
import json


def save_to_json_file(my_obj, filename):
    """ save in JSON file """
    with open(filename, mode='w') as f:
        f.write(json.dumps(my_obj))
