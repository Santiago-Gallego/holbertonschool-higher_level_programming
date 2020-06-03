#!/usr/bin/python3
""" Object from JSON"""
import json


def load_from_json_file(filename):
    """ load from json file"""
    with open(filename, 'r') as f:
        return json.load(f)
