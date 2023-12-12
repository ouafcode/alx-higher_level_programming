#!/usr/bin/python3
"""Unittest for class rectangle"""

import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_2_0(self):
        """Checking for id."""

        x0 = Rectangle(1, 2)
        self.assertEqual(x0.id, 1)
        x1 = Rectangle(2, 3)
        self.assertEqual(x1.id, 2)
        x2 = Rectangle(3, 4)
        self.assertEqual(x2.id, 3)
        x3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(x3.id, 12)
        x4 = Rectangle(10, 2, 4, 5, 34)
        self.assertEqual(x4.id, 34)
        x5 = Rectangle(10, 2, 4, 5, -5)
        self.assertEqual(x5.id, -5)
        x6 = Rectangle(10, 2, 4, 5, 9)
        self.assertEqual(x6.id, 9)

    def test_2_1(self):
        """to check attribute value."""

        x1 = Rectangle(10, 2)
        self.assertEqual(x1.width, 10)
        self.assertEqual(x1.height, 2)
        self.assertEqual(x1.x, 0)
        self.assertEqual(x1.y, 0)
        x2 = Rectangle(10, 2, 4, 5, 24)
        self.assertEqual(x2.width, 10)
        self.assertEqual(x2.height, 2)
        self.assertEqual(x2.x, 4)
        self.assertEqual(x2.y, 5)

    def test_2_2(self):
        """to check missing args."""

        with self.assertRaises(TypeError) as x:
            r0 = Rectangle(5)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'", str(
                x.exception))
        s = ("__init__() missing 2 required positional" +
             " arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle()
        self.assertEqual(s, str(x.exception))

    def test_2_3(self):
        """to check inheritance."""

        x1 = Rectangle(9, 3)
        self.assertTrue(isinstance(x1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_3_0(self):
        """ to check wrong attributes."""

        with self.assertRaises(TypeError) as x:
            r = Rectangle("Hello", 2)
        self.assertEqual("width must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(2, "World")
        self.assertEqual("height must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(1, 2, "Foo", 3)
        self.assertEqual("x must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(1, 2, 2, "Bar")
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(0, 2)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, 0)
        self.assertEqual("height must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, -3)
        self.assertEqual("height must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, 5, -5, 6)
        self.assertEqual("x must be >= 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, 8, 9, -65)
        self.assertEqual("y must be >= 0", str(x.exception))

    def test_4_0(self):
        """ To area method with correct type."""

        x1 = Rectangle(3, 2)
        self.assertEqual(x1.area(), 6)
        x2 = Rectangle(75, 2)
        self.assertEqual(x2.area(), 150)
        x3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(x3.area(), 56)

    def test_4_1(self):
        """Test for area with incorrect args."""

        with self.assertRaises(TypeError) as x:
            x1 = Rectangle(3, 2)
            x1.area("Hello")
        self.assertEqual(
            "area() takes 1 positional argument but 2 were given", str(
                x.exception))

    def test_5_0(self):
        """Test for display method."""

        f = io.StringIO()
        x1 = Rectangle(4, 5)
        with contextlib.redirect_stdout(f):
            x1.display()
        s = f.getvalue()
        tre = "####\n####\n####\n####\n####\n"
        self.assertEqual(s, tre)

    def test_5_1(self):
        """Test for display method with incorrect args."""

        with self.assertRaises(TypeError) as x:
            x1 = Rectangle(9, 6)
            x1.display(9)
        self.assertEqual(
            "display() takes 1 positional argument but 2 were given", str(
                x.exception))

    def test_6_0(self):
        """Test for __str__ representation."""

        f = io.StringIO()
        x1 = Rectangle(4, 6, 2, 1, 12)
        with contextlib.redirect_stdout(f):
            print(x1)
        s = f.getvalue()
        res = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(s, res)

    def test_7_0(self):
        """Test for display method with x and y."""

        f = io.StringIO()
        x1 = Rectangle(2, 3, 2, 2)
        with contextlib.redirect_stdout(f):
            x1.display()
        s = f.getvalue()
        res = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(s, res)

    def test_8_0(self):
        """Test for update method."""

        x1 = Rectangle(10, 10, 10, 10)
        x1.update(89)
        self.assertEqual(x1.id, 89)
        x1.update(89, 2)
        self.assertEqual(x1.width, 2)
        x1.update(89, 2, 3)
        self.assertEqual(x1.height, 3)
        x1.update(89, 2, 3, 4)
        self.assertEqual(x1.x, 4)
        x1.update(89, 2, 3, 4, 5)
        self.assertEqual(x1.y, 5)
        x1.update()
        self.assertEqual(str(x1), "[Rectangle] (89) 4/5 - 2/3")

    def test_8_1(self):
        """Test for update method with incorrect types."""

        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as x:
            r1.update("hi")
        self.assertEqual("id must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r1.update(65, 89, "hi")
        self.assertEqual("height must be an integer", str(x.exception))

    def test_9_0(self):
        """Test for  update with kwargs."""

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.height, 2)

    def test_9_1(self):
        """Test for update with incorrect types in kwargs."""

        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as x:
            r1.update(id='hi')
        self.assertEqual("id must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r1.update(height=65, x=2, width="hi")
        self.assertEqual("width must be an integer", str(x.exception))

    def test_13_0(self):
        """Test for to_dictionary method ."""

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(len(r1_dictionary), len(r_dictionary))
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(len(r1_dictionary), len(r2_dictionary))
        self.assertEqual(type(r2_dictionary), dict)
        self.assertFalse(r1 == r2)

    def test_13_1(self):
        """Test for to_dictionary with incorrect args."""

        s = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(10, 2, 1, 9)
            r1_dictionary = r1.to_dictionary("Hi")
        self.assertEqual(s, str(x.exception))


if __name__ == '__main__':
    unittest.main()
