#!/usr/bin/python3
""" This module contains print square function"""


def print_square(size):
    """
        Given  size it prints a square with #.

        Args:
            size (int): size of square
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
    """
    if not type(size) is int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for i in range(size):
            print("#", end="")
        print()
