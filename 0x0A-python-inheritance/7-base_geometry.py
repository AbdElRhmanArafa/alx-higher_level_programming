#!/usr/bin/python3
"""Write an empty class BaseGeometry."""


class BaseGeometry:
    """Improve Geometry"""
    def area(self):
        """Improve Geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Improve Geometry"""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
