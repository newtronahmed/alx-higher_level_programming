#!/usr/bin/python3
""" Module Square"""


class Square:
    """Square class defined by geometric shape
     - Private instance attribute: size.
     - Instantiation with size (no type/value verification).
    Attributes:
        size (int): Size of square
    """

    def __init__(self, size=0):
        """
        Initialize method
        Args:
            size (int): int to assign to square size
        Raises:
            TypeError: if size is not int
            ValueError: size less than 0
        """
        if not isinstance(size, int):  # if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
