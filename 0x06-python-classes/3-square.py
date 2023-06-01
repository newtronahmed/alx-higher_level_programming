#!/usr/bin/python3
""" Module Square"""


class Square:
    """Square class defined by geometric shape
     - Private instance attribute: size.
     - Instantiation with optional size.
     - Public instance method: def area(self).
     Attributes:
            size (int): Size of square
    """

    def __init__(self, size=0):
        """Initialize method
        Args:
            size (int): size of a side of the square
        Raises:
            TypeError: if size is not int
            ValueError: size less than 0
        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square
        Return:
            Current square area (int)
        """
        return self.__size ** 2
