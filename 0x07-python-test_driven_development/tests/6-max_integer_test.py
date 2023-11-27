#!/usr/bin/python3
""" unitests for max_integer function """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ write for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list"""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_beggining(self):
        """Test a list with a beginning max value."""
        max_beggining = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_beggining), 4)

    def test_empty(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_floats(self):
        """Test a list of ints and floats."""
        ints_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_str(self):
        """Test a list of strings."""
        str = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(str), "name")

    def test_empty(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
