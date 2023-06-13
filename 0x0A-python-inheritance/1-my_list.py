#!/usr/bin/python3
"""This module contains print_sorted function"""


class MyList(list):
    """My list class that inherits list built in"""
    def print_sorted(self):
        """prints list in ascending order"""
        print(sorted(self))
