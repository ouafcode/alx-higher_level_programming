#!/usr/bin/python3
"""Unittest for class square"""

import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test class for Square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_10_0(self):
        """Test to check for attributes."""

        x0 = Square(1)
        self.assertEqual(x0.id, 1)
        x1 = Square(5, 3, 4)
        self.assertEqual(x1.height, 5)
        self.assertEqual(x1.width, 5)
        self.assertEqual(x1.x, 3)
        self.assertEqual(x1.y, 4)
        self.assertEqual(x1.id, 2)

    def test_10_1(self):
        """Test __str__ representation."""

        x1 = Square(9, 4, 5, 6)
        self.assertEqual(str(x1), "[Square] (6) 4/5 - 9")

    def test_10_2(self):
        """Test to check for inheritance."""

        x1 = Square(6)
        self.assertTrue(isinstance(x1, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(x1, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

    def test_10_3(self):
        """Test to check for missing args."""

        with self.assertRaises(TypeError) as x:
            s1 = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'", str(
                x.exception))

    def test_10_4(self):
        """Test inherited from Rectangle."""

        x1 = Square(9)
        self.assertEqual(x1.area(), 81)
        x2 = Square(4, 1, 2, 5)
        x2.update(7)
        self.assertEqual(x2.id, 7)
        f = io.StringIO()
        x3 = Square(4)
        with contextlib.redirect_stdout(f):
            x3.display()
        s = f.getvalue()
        res = "####\n####\n####\n####\n"
        self.assertEqual(s, res)

    def test_11_0(self):
        """Test to check for size attribute."""

        x1 = Square(8)
        self.assertEqual(x1.size, 8)
        x2 = Square(9, 8, 7, 2)
        self.assertEqual(x2.size, 9)

    def test_11_1(self):
        """Test to check for incorrect attributes."""

        with self.assertRaises(TypeError) as x:
            s = Square("Hello", 2)
        self.assertEqual("width must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s = Square(2, "World")
        self.assertEqual("x must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s = Square(1, 2, "Foo", 3)
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(0, 2)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(-1)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(2, -3)
        self.assertEqual("x must be >= 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(2, 5, -5, 6)
        self.assertEqual("y must be >= 0", str(x.exception))

    def test_12_0(self):
        """Test to check update method"""

        x1 = Square(5)
        x1.update(10)
        self.assertEqual(x1.id, 10)
        x1.update(x=12)
        self.assertEqual(x1.x, 12)
        x1.update(size=7, id=89, y=1)
        self.assertEqual(x1.size, 7)
        self.assertEqual(x1.id, 89)
        self.assertEqual(x1.y, 1)
        x1.update()
        self.assertEqual(x1.size, 7)
        self.assertEqual(x1.id, 89)
        self.assertEqual(x1.y, 1)

    def test_12_1(self):
        """Test for update method with incorrect types."""

        x1 = Square(9)
        with self.assertRaises(TypeError) as x:
            x1.update(2, 3, 4, "hello")
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            x1.update("hello", 8, 9)
        self.assertEqual("id must be an integer", str(x.exception))

    def test_14_0(self):
        """Test for public method to_dictionary."""

        x1 = Square(10, 2, 1)
        x1_dictionary = x1.to_dictionary()
        s_dictionary = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertEqual(len(x1_dictionary), len(s_dictionary))
        self.assertEqual(type(x1_dictionary), dict)
        x2 = Square(1, 1)
        x2.update(**x1_dictionary)
        x2_dictionary = x2.to_dictionary()
        self.assertEqual(len(x1_dictionary), len(x2_dictionary))
        self.assertEqual(type(x2_dictionary), dict)
        self.assertFalse(x1 == x2)

    def test_14_1(self):
        """Test to_dictionary  method with incorrect args."""

        s = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            x1 = Square(10, 2, 1, 9)
            x1_dictionary = x1.to_dictionary("Hi")
        self.assertEqual(s, str(x.exception))


if __name__ == "__main__":
    unittest.main()
