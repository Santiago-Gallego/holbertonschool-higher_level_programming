#!/usr/bin/python3
"""
This test is for the base class
Type: Unittest
Functions:
"""
import unittest
from models.base import Base as B
from models.rectangle import Rectangle as R
from models.square import Square as S


class t_Base_class(unittest.TestCase):
    """Base class unit test"""

    def test_id_input(self):
        """checking the entry of the id argument"""
        B._Base__nb_objects = 0

        b1 = B()
        self.assertEqual(b1.id, 1)

        b2 = B(17)
        self.assertEqual(b2.id, 17)

        b3 = B(-17)
        self.assertEqual(b3.id, -17)

    def test_id_plusplus(self):
        """checking the increase of the id argument"""
        B._Base__nb_objects = 0

        b4 = B()
        self.assertEqual(b4.id, 1)

        b5 = B()
        self.assertEqual(b5.id, 2)

        b6 = B()
        self.assertEqual(b6.id, 3)

        b7 = B(5)
        b8 = B()
        self.assertEqual(b8.id, 4)

        b9 = B()
        self.assertEqual(b9.id, 5)

    def test_to_json_string(self):
        """
        check JSON string representation of dictionary list.
        """
        r1 = R(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = B.to_json_string([dictionary])
        self.assertCountEqual(
            dictionary, {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)

    def test_save_to_file(self):
        """
        check if save a obj as JSON string in json file
        """
        r1 = R(10, 7, 2, 8)
        r2 = R(2, 4)
        R.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            txt = file.read()

    def test_create(self):
        """
        check if return a instance with all attributes already set.
        """
        d1 = {'id': 10, 'size': 6, 'x': 17, 'y': 17}
        s1 = S.create(**d1)
        self.assertEqual(s1.to_dictionary(), d1)
        self.assertEqual(B._Base__nb_objects, 1)

        d2 = {'id': 5, 'width': 3, 'height': 7, 'x': 2, 'y': 1}
        r1 = R.create(**d2)
        self.assertEqual(r1.to_dictionary(), d2)
        self.assertEqual(B._Base__nb_objects, 2)

        r3 = R(6, 3)
        d3 = r3.to_dictionary()
        r4 = R.create(**d3)
        self.assertEqual(r4.to_dictionary(), d3)
        self.assertEqual(B._Base__nb_objects, 4)

        s2 = S(5)
        d4 = s2.to_dictionary()
        s5 = S.create(**d4)
        self.assertEqual(s5.to_dictionary(), d4)
        self.assertEqual(B._Base__nb_objects, 6)

    def test_load_from_file(self):
        """check id return a list of instances"""
        r5 = R(6, 3)
        d5 = r5.to_dictionary()
        R.save_to_file([r5])
        l_o = R.load_from_file()
        self.assertIsInstance(l_o[0], R)
        self.assertDictEqual(l_o[0].to_dictionary(), d5)

        s6 = S(6)
        d6 = s6.to_dictionary()
        S.save_to_file([s6])
        l_o2 = S.load_from_file()
        self.assertIsInstance(l_o2[0], S)
        self.assertDictEqual(l_o2[0].to_dictionary(), d6)

        R.save_to_file([r5, r5, r5])
        l_o3 = R.load_from_file()
        S.save_to_file([s6, s6, s6])
        l_o4 = S.load_from_file()

        self.assertIsInstance(l_o3[1], R)
        self.assertDictEqual(l_o3[1].to_dictionary(), d5)

        self.assertIsInstance(l_o4[2], R)
        self.assertDictEqual(l_o4[2].to_dictionary(), d6)
