#!/usr/bin/python3
""" Test is for the base class """


import unittest
import json
import pep8
from models import base
Base = base.Base


class TestDocs(unittest.TestCase):
    """ Test for check all the documentation """
    def testDocString(self):
        """Tests for the module docstring"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_ClassDocstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_pep8_Test_base(self):
        """Test that tests/test_models/test_base.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestBase(unittest.TestCase):
    """ Class for the test of the class base """
    def test_moreArguments(self):
        """ When its passes more arguments
        than the required """
        with self.assertRaises(TypeError):
            base = Base(1, 1)

    def test_whenNoIdPassed(self):
        """ When there is no Id passed """
        base = Base()
        self.assertEqual(base.id, 1)

    def test_whenIdIsPassed(self):
        """ When there is Id passed """
        base = Base(74)
        self.assertEqual(base.id, 74)

    def test_theNbPrivate(self):
        """ Test if __nb_objects is private """
        base = Base(56)
        with self.assertRaises(AttributeError):
            print(base.nb_objects)
        with self.assertRaises(AttributeError):
            print(base.__nb_objects)

    def test_ToJsonStringIsEmpty(self):
        """ Test when is passed an empty list
        or Nothing """
        json_str = Base.to_json_string([])
        self.assertTrue(type(json_str) is str)
        self.assertEqual(json_str, "[]")

    def test_ToJsonString(self):
        """ Test if works well the method """
        Base._Base__nb_objects = 0
        ob1 = {"id": 12, "width": 4, "height": 3, "x": 8, "y": 12}
        ob2 = {"id": 14, "width": 6, "height": 2, "x": 4, "y": 3}
        json_str = Base.to_json_string([ob1, ob2])
        self.assertTrue(type(json_str) is str)
        ob = json.loads(json_str)
        self.assertEqual(ob, [ob1, ob2])

    def test_NoneToJsonString(self):
        """ Test when None is passed """
        json_str = Base.to_json_string(None)
        self.assertTrue(type(json_str) is str)
        self.assertEqual(json_str, "[]")

    def test_FromJsonString(self):
        """ Test if work well the method """
        json_str = '[{"id": 12, "width": 4, "height": 3, "x": 8, "y": 12}, \
{"id": 14, "width": 6, "height": 2, "x": 4, "y": 3}]'
        json_list = Base.from_json_string(json_str)
        self.assertTrue(type(json_list) is list)
        self.assertEqual(len(json_list), 2)
        self.assertTrue(type(json_list[0]) is dict)
        self.assertTrue(type(json_list[1]) is dict)
        self.assertEqual(json_list[0], {"id": 12, "width": 4, "height": 3,
                                        "x": 8, "y": 12})
        self.assertEqual(json_list[1], {"id": 14, "width": 6, "height": 2,
                                        "x": 4, "y": 3})

    def test_FromJsonStringNone(self):
        """ Test the method with an empty string """
        self.assertEqual([], Base.from_json_string(None))

    def test_FromJsonStringEmpty(self):
        """ Test the method with an empty string """
        self.assertEqual([], Base.from_json_string(""))
