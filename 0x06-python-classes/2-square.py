#!/usr/bin/python3
# 2-square.py
"""Define a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
            TypeError: size not an integer
            ValueError:size being < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
