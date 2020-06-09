#!/usr/bin/python3
""" Test is for the square class """
import unittest
from models.base import Base as B
from models.rectangle import Rectangle as R
from models.square import Square as S
import sys
from io import StringIO


class Test_Saquare_class(unittest.TestCase):
    """ Test rectangle class """

    def test_id_input(self):
        """ Test id argument """
        B._Base__nb_objects = 0

        s1 = S(6)
        self.assertEqual(s1.id, 1)

        s2 = S(6, 0, 0, 17)
        self.assertEqual(s2.id, 17)

        s3 = S(6, 0, 0, -17)
        self.assertEqual(s3.id, -17)

    def test_id_plusplus(self):
        """ Test increase id argument """
        B._Base__nb_objects = 0

        s4 = S(6)
        self.assertEqual(s4.id, 1)

        s5 = S(6)
        self.assertEqual(s5.id, 2)

        s6 = S(6)
        self.assertEqual(s6.id, 3)

        s7 = S(6, 0, 0, 5)
        s8 = S(6)
        self.assertEqual(s8.id, 4)

        s9 = S(6)
        self.assertEqual(s9.id, 5)

    def test_area(self):
        """ Test function area """
        s10 = S(5)
        self.assertEqual(s10.area(), 25)

    def test_display(self):
        """ Test display method """
        new_output = StringIO()
        sys.stdout = new_output
        s11 = S(2)
        s11.display()
        sys.stdout = sys.__stdout__
        assert new_output.getvalue() == "##\n##\n"

    def test_str(self):
        """ Test str method """
        new_output = StringIO()
        sys.stdout = new_output
        s12 = S(5, 2, 5)
        print(s12)
        sys.stdout = sys.__stdout__
        self.assertEqual(new_output.getvalue(), "[Square] (6) 2/5 - 5\n")

    def test_update(self):
        """ Test update method """
        new_output = StringIO()
        sys.stdout = new_output
        s13 = S(5)
        s13.update(10)
        s13.update(1, 2)
        s13.update(1, 2, 3)
        s13.update(1, 2, 3, 4)
        s13.update(x=12)
        s13.update(size=7, y=1)
        s13.update(size=7, id=89, y=1)
        print(s13)
        sys.stdout = sys.__stdout__
        assert new_output.getvalue() == "[Square] (89) 12/1 - 7\n"
