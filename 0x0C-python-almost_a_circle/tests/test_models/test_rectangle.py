#!/usr/bin/python3
"""
This test is for the Rectangle class
Type: Unittest
Functions:
"""
import unittest
from models.base import Base as B
from models.rectangle import Rectangle as R
from models.square import Square as S
import sys
from io import StringIO


class t_Rectangle_class(unittest.TestCase):
    """Rectangle unit tests"""

    def test_id_input(self):
        """checking the entry of the id argument"""
        B._Base__nb_objects = 0

        r6 = R(6, 3)
        self.assertEqual(r6.id, 1)

        r7 = R(6, 3, 0, 0, 17)
        self.assertEqual(r7.id, 17)

        r8 = R(6, 3, 0, 0, -17)
        self.assertEqual(r8.id, -17)

    def test_id_plusplus(self):
        """checking the increase of the id argument"""
        B._Base__nb_objects = 0

        r9 = R(6, 3)
        self.assertEqual(r9.id, 1)

        r10 = R(6, 3)
        self.assertEqual(r10.id, 2)

        r11 = R(6, 3)
        self.assertEqual(r11.id, 3)

        r12 = R(6, 3, 0, 0, 5)
        r13 = R(6, 3)
        self.assertEqual(r13.id, 4)

        r14 = R(6, 3)
        self.assertEqual(r14.id, 5)

    def test_property_exceptions(self):
        """"checking propertys"""
        r15 = R(6, 3)
        self.assertEqual(r15.width, 6)
        self.assertRaisesRegex(
                TypeError,
                'width must be an integer',
                R,
                'k', 3, 0, 0, 17
                )
        self.assertRaisesRegex(
                ValueError,
                'width must be > 0',
                R,
                -6, 3, 0, 0, 17
                )

        r16 = R(6, 3)
        self.assertEqual(r16.height, 3)
        self.assertRaisesRegex(
                TypeError,
                'height must be an integer',
                R,
                6, 'k', 0, 0, 17
                )
        self.assertRaisesRegex(
                ValueError,
                'height must be > 0',
                R,
                6, -3, 0, 0, 17
                )

        r17 = R(6, 3, 1, 2)
        self.assertEqual(r17.x, 1)
        self.assertRaisesRegex(
                TypeError,
                'x must be an integer',
                R,
                6, 3, 'k', 2, 17
                )
        self.assertRaisesRegex(
                ValueError,
                'x must be >= 0',
                R,
                6, 3, -1, 2, 17
                )

        r18 = R(6, 3, 1, 2)
        self.assertEqual(r18.y, 2)
        self.assertRaisesRegex(
                TypeError,
                'y must be an integer',
                R,
                6, 3, 1, 'k', 17
                )
        self.assertRaisesRegex(
                ValueError,
                'y must be >= 0',
                R,
                6, 3, 1, -2, 17
            )

    def test_area(self):
        """check function area"""
        r19 = R(6, 3)
        self.assertEqual(r19.area(), 18)

    def test_display(self):
        """check display method"""
        new_output = StringIO()
        sys.stdout = new_output
        r20 = R(3, 2)
        r20.display()
        sys.stdout = sys.__stdout__
        assert new_output.getvalue() == "###\n###\n"

    def test_str(self):
        """check str method"""
        new_output = StringIO()
        sys.stdout = new_output
        r21 = R(4, 6, 2, 1, 12)
        print(r21)
        sys.stdout = sys.__stdout__
        assert new_output.getvalue() == "[Rectangle] (12) 2/1 - 4/6\n"

    def test_update(self):
        """check update method"""
        new_output = StringIO()
        sys.stdout = new_output
        r22 = R(10, 10, 10, 10)
        r22.update(89)
        r22.update(89, 2)
        r22.update(89, 2, 3)
        r22.update(89, 2, 3, 4)
        r22.update(89, 2, 3, 4, 5)
        print(r22)
        sys.stdout = sys.__stdout__
        assert new_output.getvalue() == "[Rectangle] (89) 4/5 - 2/3\n"
