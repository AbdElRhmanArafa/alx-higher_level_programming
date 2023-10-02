#!/usr/bin/python3
'''
Contains a max_integer function for a TDD project.
'''

import unittest

from .6-max_integer import max_integer


class MaxIntegerTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_list_with_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_list_with_multiple_elements(self):
        self.assertEqual(max_integer([1, 5, 3, 2, 4]), 5)

    def test_list_with_negative_elements(self):
        self.assertEqual(max_integer([-1, -5, -3, -2, -4]), -1)

    def test_list_with_duplicate_elements(self):
        self.assertEqual(max_integer([1, 1, 5, 3, 2]), 5)

    def test_float_elements(self):
        self.assertEqual(max_integer([1.5, 5.5, 3.3, 2.2, 4.4]), 5.5)

    def test_string_elements(self):
        with self.assertRaises(TypeError):
            max_integer(["hello", "world", "foo"])

    def test_mixed_types(self):
        self.assertEqual(max_integer([1, "hello", 5.5, 3, 2]), 5.5)

if __name__ == "__main__":
    unittest.main()
