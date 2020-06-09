#!/usr/bin/python3
""" this is the module base """
import json
import os
import csv


class Base():
    """ Private attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize attribute """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ String representation of dictionary list """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        for item in list_dictionaries:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save a obj as JSON """
        list_obj = []
        if list_objs is None:
            list_obj = []
        else:
            for obj_c in list_objs:
                list_obj.append(obj_c.to_dictionary())
        with open(cls.__name__ + '.json', 'w') as file_:
            file_.write(cls.to_json_string(list_obj))

    @staticmethod
    def from_json_string(json_string):
        """ Return dictionary list """
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return a instance with all attributes """
        if cls.__name__ == 'Square':
            new_instance = cls(1)
        else:
            new_instance = cls(1, 1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """ Return a list of instances """
        f_name = cls.__name__ + '.json'
        l_i = []
        if not os.path.exists(f_name):
            return []
        with open(f_name, 'r', encoding='utf-8') as j_f:
            l_d = cls.from_json_string(j_f.read())
        for d in l_d:
            l_i.append(cls.create(**d))
        return l_i
