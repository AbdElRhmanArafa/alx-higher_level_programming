#!/usr/bin/python3
"""
The 0-add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
      a: An integer or float.
      b: An integer or float.

    Returns:
      An integer: the addition of a and b.

    Raises:
      TypeError: If a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
