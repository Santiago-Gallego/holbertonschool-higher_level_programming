#!/usr/bin/python3
"""
This test is for the square class
Type: Unittest
Functions:
"""
import unittest
from models.base import Base as B
from models.rectangle import Rectangle as R
from models.square import Square as S
import sys
from io import StringIO


class t_Saquare_class(unittest.TestCase):
    """Rectangle unit tests"""

    def test_id_input(self):
        """checking the entry of the id argument"""
        B._Base__nb_objects = 0

        s6 = S(6)
        self.assertEqual(s6.id, 1)

        s7 = S(6, 0, 0, 17)
        self.assertEqual(s7.id, 17)

        s8 = S(6, 0, 0, -17)
        self.assertEqual(s8.id, -17)

    def test_id_plusplus(self):
        """checking the increase of the id argument"""
        B._Base__nb_objects = 0

        s9 = S(6)
        self.assertEqual(s9.id, 1)

        s10 = S(6)
        self.assertEqual(s10.id, 2)

        s11 = S(6)
        self.assertEqual(s11.id, 3)

        s12 = S(6, 0, 0, 5)
        s13 = S(6)
        self.assertEqual(s13.id, 4)

        s14 = S(6)
        self.assertEqual(s14.id, 5)

    def test_property_exceptions(self):
        """"checking propertys"""
        s15 = S(6)
        self.assertEqual(s15.size, 6)
        self.assertRaisesRegex(
                TypeError,
                'width must be an integer',
                S,
                'k', 0, 0, 17
                )
        self.assertRaisesRegex(
                ValueError,
                'width must be > 0',
                S,
                -6, 0, 0, 17
                )

        s17 = S(6, 1, 2)
        self.assertEqual(s17.x, 1)
        self.assertRaisesRegex(
                TypeError,
                'x must be an integer',
                S,
                6, 'k', 2, 17
                )
        self.assertRaisesRegex(
                ValueError,
                'x must be >= 0',
                S,
                6, -1, 2, 17
                )

        s18 = S(6, 1, 2)
        self.assertEqual(s18.y, 2)
        self.assertRaisesRegex(
                TypeError,
                'y must be an integer',
                S,
                6, 1, 'k', 17
                )
        self.assertRaisesRegex(
                ValueError,
                'y must be >= 0',
                S,
                6, 1, -2, 17
            )

    def test_area(self):
        """check function area"""
        s19 = S(6)
        self.assertEqual(s19.area(), 36)

    def test_display(self):
        """check display method"""
        new_output = StringIO()
        sys.stdout = new_output
        s20 = S(2)
        s20.display()
        sys.stdout = sys.__stdout__
        assert new_output.getvalue() == "##\n##\n"

    def test_str(self):
        """check str method"""
        new_output = StringIO()
        sys.stdout = new_output
        s21 = S(3, 1, 3)
        print(s21)
        sys.stdout = sys.__stdout__
        self.assertEqual(new_output.getvalue(), "[Square] (9) 1/3 - 3\n")

    def test_update(self):
        """check update method"""
        new_output = StringIO()
        sys.stdout = new_output
        s22 = S(5)
        s22.update(10)
        s22.update(1, 2)
        s22.update(1, 2, 3)
        s22.update(1, 2, 3, 4)
        s22.update(x=12)
        s22.update(size=7, y=1)
        s22.update(size=7, id=89, y=1)
        print(s22)
        sys.stdout = sys.__stdout__
        assert new_output.getvalue() == "[Square] (89) 12/1 - 7\n"
