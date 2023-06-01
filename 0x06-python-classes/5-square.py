#!/usr/bin/python3
""" Module Square"""


class Square:
    """Represents a square.
    - Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    - Instantiation with optional size.
    - Public instance method: def area(self).
    - Public instance method: def my_print(self).
    Attributes:
        size (int): Size of square
    """

    def __init__(self, size=0):
        """Initialize method
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.__size = size

    @property
    def size(self):
        """
        getter of size
        Return:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of size
        Args:
            value (int): size of a side of the square
        Raises
            TypeError: if size is not int
            ValueError: size less than 0
        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square
        Return:
            Current square area (int)
        """
        return self.__size ** 2

    def my_print(self):
        """Print a square from the size using #
        Returns:
            None
        """

        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                print("#" * self.__size)
