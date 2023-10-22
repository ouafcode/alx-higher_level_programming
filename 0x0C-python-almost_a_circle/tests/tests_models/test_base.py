#!/usr/bin/python3
"""Unit tests for models/base.py"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """for testing base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_1_0(self):
        """ to check for id"""

        s0 = Base()
        self.assertEqual(s0.id, 1)
        s1 = Base()
        self.assertEqual(s1.id, 2)
        s2 = Base(12)
        self.assertEqual(s2.id, 12)
        s3 = Base(0)
        self.assertEqual(s3.id, 0)
        s4 = Base(927)
        self.assertEqual(s4.id, 927)
        s5 = Base(-5)
        self.assertEqual(s5.id, -5)
        s6 = Base(9)
        self.assertEqual(s6.id, 9)

    def test_1_1(self):
        """ to test type """

        s6 = Base()
        self.assertEqual(type(s6), Base)
        self.assertTrue(isinstance(s6, Base))

    def test_15_0(self):
        """Test to_json_string method """

        dt = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_d = Base.to_json_string([dt])
        self.assertTrue(isinstance(dt, dict))
        self.assertTrue(isinstance(json_d, str))
        self.assertCountEqual(
            json_d, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')
        json_d_1 = Base.to_json_string([])
        self.assertEqual(json_d_1, "[]")
        json_d_2 = Base.to_json_string(None)
        self.assertEqual(json_d_1, "[]")

    def test_15_1(self):
        """Test to_json_string with incorrect type"""

        with self.assertRaises(TypeError) as x:
            Base.to_json_string(9)
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string("Hello")
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string(["Hi", "Here"])
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string(7.8)
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string([2, 1, 3, 4])
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string({1: 'hi', 2: 'there'})
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string((9, 0))
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string(True)
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))

    def test_15_2(self):
        """Test to_json_string with incorrect number of args."""

        s1 = ("to_json_string() missing 1 required positional argument: " +
              "'list_dictionaries'")
        with self.assertRaises(TypeError) as x:
            Base.to_json_string()
        self.assertEqual(s1, str(x.exception))
        s2 = "to_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            Base.to_json_string([{1, 2}], [{3, 4}])
        self.assertEqual(s2, str(x.exception))

    def test_16_0(self):
        """Test save_to_file class with normal type"""

        x0 = Rectangle(10, 7, 2, 8)
        x1 = Rectangle(2, 4)
        Rectangle.save_to_file([x0, x1])
        dictr = ('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},' +
               ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), len(dictr))
        Rectangle.save_to_file(None)
        dictr = "[]"
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), dictr)
        os.remove("Rectangle.json")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), dictr)
        s0 = Square(9, 3, 1, 12)
        s1 = Square(6, 7)
        Square.save_to_file([s0, s1])
        dictr = ('[{"id": 12, "size": 9, "x": 3, "y": 1},' +
               ' {"id": 3, "size": 6, "x": 7, "y": 0}]')
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), len(dictr))
        Square.save_to_file(None)
        dictr = "[]"
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), dictr)
        os.remove("Square.json")
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), dictr)

    def test_16_1(self):
        """Test save_to_file method with error."""

        with self.assertRaises(AttributeError) as x:
            Base.save_to_file([Base(9), Base(5)])
        self.assertEqual(
            "'Base' object has no attribute 'to_dictionary'", str(
                x.exception))
        with self.assertRaises(AttributeError) as x:
            Rectangle.save_to_file([3, 4])
        self.assertEqual(
            "'int' object has no attribute 'to_dictionary'", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file(5)
        self.assertEqual(
            "'int' object is not iterable", str(
                x.exception))

    def test_16_2(self):
        """Test save_to_file with incorrect args."""

        x1 = ("save_to_file() missing 1 required" +
              " positional argument: 'list_objs'")
        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file()
        self.assertEqual(x1, str(x.exception))
        x2 = ("save_to_file() takes 2 positional" +
              " arguments but 3 were given")
        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file([Rectangle(9, 4), Rectangle(8, 9)], 98)
        self.assertEqual(x2, str(x.exception))

    def test_17_0(self):
        """Test from_json_string with correct types."""

        lst_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_input = Rectangle.to_json_string(lst_input)
        list_output = Rectangle.from_json_string(json_input)
        res = [{'width': 10, 'height': 4, 'id': 89},
               {'width': 1, 'height': 7, 'id': 7}]
        self.assertCountEqual(list_output, res)
        self.assertEqual(type(list_output), list)

        list_output_1 = Rectangle.from_json_string('')
        self.assertEqual(list_output_1, [])

        list_output_2 = Rectangle.from_json_string(None)
        self.assertEqual(list_output_2, [])

    def test_17_1(self):
        """Test from_json_string with incorrect type."""

        with self.assertRaises(TypeError) as x:
            list_output = Rectangle.from_json_string([8, 9])
        self.assertEqual("json_string must be a string", str(x.exception))
        with self.assertRaises(TypeError) as x:
            list_output = Rectangle.from_json_string(8)
        self.assertEqual("json_string must be a string", str(x.exception))
        with self.assertRaises(TypeError) as x:
            list_output = Rectangle.from_json_string(9.6)
        self.assertEqual("json_string must be a string", str(x.exception))
        with self.assertRaises(TypeError) as x:
            list_output = Rectangle.from_json_string((4, 5))
        self.assertEqual("json_string must be a string", str(x.exception))
        with self.assertRaises(TypeError) as x:
            list_output = Rectangle.from_json_string({1: 'Hello', 2: 'Hi'})
        self.assertEqual("json_string must be a string", str(x.exception))

    def test_17_2(self):
        """Test from_json_string with incorrect args."""

        x1 = ("from_json_string() missing 1" +
              " required positional argument: 'json_string'")
        with self.assertRaises(TypeError) as x:
            Rectangle.from_json_string()
        self.assertEqual(x1, str(x.exception))
        x2 = "from_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            Rectangle.from_json_string("Hi", 98)
        self.assertEqual(x2, str(x.exception))

    def test_18_0(self):
        """Test create with correcte types."""

        t1 = Rectangle(3, 5, 1)
        r1_dictionary = t1.to_dictionary()
        t2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(t1), str(t2))
        self.assertFalse(t1 is t2)
        self.assertFalse(t1 == t2)
        s1 = Square(3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_18_1(self):
        """Test create with incorrecte types."""

        with self.assertRaises(TypeError) as x:
            x1 = "Hello"
            x2 = Rectangle.create(x1)
        self.assertEqual(
            "create() takes 1 positional argument but 2 were given", str(
                x.exception))

    def test_19_0(self):
        """Test load_from_file with correcte types."""

        x1 = Rectangle(10, 7, 2, 8)
        x2 = Rectangle(2, 4)
        list_rectangles_input = [x1, x2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        for x in zip(list_rectangles_input, list_rectangles_output):
            self.assertEqual(str(x[0]), str(x[1]))

        s1 = Square(10, 2)
        s2 = Square(9)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        for x in zip(list_squares_input, list_squares_output):
            self.assertEqual(str(x[0]), str(x[1]))

    def test_19_1(self):
        """Test load_from_file without file files."""

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, [])

    def test_19_2(self):
        """Test load_from_file with incorrect args."""

        s = "load_from_file() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            list_rectangles_output = Rectangle.load_from_file("Hello")
        self.assertEqual(s, str(x.exception))

    def test_20_0(self):
        """Test save_to_file_csv with correcte types."""

        r0 = Rectangle(10, 7, 2, 8)
        r1 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r0, r1])
        res = "id,width,height,x,y\n1,10,7,2,8\n2,2,4,0,0\n"
        with open("Rectangle.csv", "r") as f:
            self.assertEqual(len(f.read()), len(res))
        s0 = Square(9, 3, 1, 12)
        s1 = Square(6, 7)
        Square.save_to_file_csv([s0, s1])
        res = "id,size,x,y\n12,9,3,1\n3,6,7,0\n"
        with open("Square.csv", "r") as f:
            self.assertEqual(len(f.read()), len(res))

    def test_20_1(self):
        """Test ave_to_file_csv with errors."""

        with self.assertRaises(AttributeError) as x:
            Base.save_to_file_csv([Base(9), Base(5)])
        self.assertEqual(
            "'Base' object has no attribute 'to_dictionary'", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file_csv([3, 4])
        self.assertEqual(
            "list_objs must be a list of instances", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file_csv(5.9)
        self.assertEqual(
            "list_objs must be a list of instances", str(
                x.exception))

    def test_20_2(self):
        """Test save_to_file_csv with incorrect args."""

        s1 = ("save_to_file_csv() missing 1 required" +
              " positional argument: 'list_objs'")
        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file_csv()
        self.assertEqual(s1, str(x.exception))
        s2 = "save_to_file_csv() takes 2 positional arguments but 3 were given"
        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file_csv([Rectangle(9, 4), Rectangle(8, 9)], 98)
        self.assertEqual(s2, str(x.exception))

    def test_20_3(self):
        """Test load_from_file_csv with correct types."""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        for x in zip(list_rectangles_input, list_rectangles_output):
            self.assertEqual(str(x[0]), str(x[1]))

        s1 = Square(10, 2)
        s2 = Square(9)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        for x in zip(list_squares_input, list_squares_output):
            self.assertEqual(str(x[0]), str(x[1]))

    def test_20_4(self):
        """Test class method load_from_file_csv with missing files."""

        os.remove("Rectangle.csv")
        os.remove("Square.csv")
        os.remove("Base.csv")
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(list_rectangles_output, [])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(list_squares_output, [])

    def test_20_5(self):
        """Test load_from_file_csv with incorrect args."""

        s = "load_from_file_csv() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            list_rectangles_output = Rectangle.load_from_file_csv("Hello")
        self.assertEqual(s, str(x.exception))


if __name__ == "__main__":
    unittest.main()
