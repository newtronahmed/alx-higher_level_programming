#!/usr/bin/python3
""" Module Square"""


class Square:
    """Square class defined by geometric shap
     - Private instance attribute: size.
     - Instantiation with size (no type/value verification).
    Attributes:
        size (int): Size of square
    """

    def __init__(self, size):
        """Initialize methode
        Args:
            size (int): size of square
        """

        #: int: __size attribute for size
        self.__size = size
