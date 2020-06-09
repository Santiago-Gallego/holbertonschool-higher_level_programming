#!/usr/bin/python3
""" Test is for the Rectangle class """
import unittest
from models.base import Base as B
from models.rectangle import Rectangle as R
from models.square import Square as S
import sys
from io import StringIO


class t_Rectangle_class(unittest.TestCase):
    """ Test rectangle class """

    def test_id_input(self):
        """ test id argument"""
        B._Base__nb_objects = 0

        r1 = R(6, 3)
        self.assertEqual(r1.id, 1)

        r2 = R(6, 3, 0, 0, 17)
        self.assertEqual(r2.id, 17)

        r3 = R(6, 3, 0, 0, -17)
        self.assertEqual(r3.id, -17)

    def test_id_increase (self):
        """ Test increase id argument"""
        B._Base__nb_objects = 0

        r4 = R(6, 3)
        self.assertEqual(r4.id, 1)

        r5 = R(6, 3)
        self.assertEqual(r5.id, 2)

        r6 = R(6, 3)
        self.assertEqual(r6.id, 3)

        r7 = R(6, 3, 0, 0, 5)
        r8 = R(6, 3)
        self.assertEqual(r8.id, 4)

        r9 = R(6, 3)
        self.assertEqual(r9.id, 5)

    def test_area(self):
        """ Test function area """
        r10 = R(6, 3)
        self.assertEqual(r10.area(), 18)

    def test_display(self):
        """ Test display method """
        new_output = StringIO()
        sys.stdout = new_output
        r11 = R(3, 2)
        r11.display()
        sys.stdout = sys.__stdout__
        assert new_output.getvalue() == "###\n###\n"

    def test_str(self):
        """ Test str method """
        new_output = StringIO()
        sys.stdout = new_output
        r12 = R(4, 6, 2, 1, 12)
        print(r12)
        sys.stdout = sys.__stdout__
        assert new_output.getvalue() == "[Rectangle] (12) 2/1 - 4/6\n"

    def test_update(self):
        """ Test update method """
        new_output = StringIO()
        sys.stdout = new_output
        r13 = R(10, 10, 10, 10)
        r13.update(89)
        r13.update(89, 2)
        r13.update(89, 2, 3)
        r13.update(89, 2, 3, 4)
        r13.update(89, 2, 3, 4, 5)
        print(r13)
        sys.stdout = sys.__stdout__
        assert new_output.getvalue() == "[Rectangle] (89) 4/5 - 2/3\n"
