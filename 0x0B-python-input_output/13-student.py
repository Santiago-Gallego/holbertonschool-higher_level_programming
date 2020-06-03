#!/usr/bin/python3
""" class Student that defines a student """


class Student:
    """ class Student """
    def __init__(self, first_name="", last_name="", age=""):
        """ init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to_json """
        a_dict = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if hasattr(self, i):
                a_dict[i] = getattr(self, i)
        return a_dict

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for i, j in json.items():
            if hasattr(self, i):
                setattr(self, i, j)
