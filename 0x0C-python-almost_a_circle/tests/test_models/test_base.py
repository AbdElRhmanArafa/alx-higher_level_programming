#!/usr/bin/python3
"""Defines unittests for base.py."""
import unittest
from models.base import Base

class TestBaseInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        """Test creating Base instances with no arguments."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        """Test creating three Base instances."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        """Test creating Base instances with None as id."""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        """Test creating Base instances with unique id."""
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        """Test the number of instances after creating with unique id."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        """Test modifying the id attribute."""
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    # Add more test cases for different data types and edge cases

    def test_str_id(self):
        """Test creating Base instances with str as id."""
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        """Test creating Base instances with float as id."""
        self.assertEqual(5.5, Base(5.5).id)

 
    def test_two_args(self):
        """Test creating Base instances with two arguments."""
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == '__main__':
    unittest.main()
