#!/usr/bin/python3
"""This module contains the Rectangle class"""


class Rectangle:
    """This is the rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        rect = ""
        for i in range(self.__height):
            for i in range(self.__width):
                rect += "#"
            rect+="\n"
        return rect
    @property
    def width(self):
        """Getter function of the width prop"""
        return self.__width
    @width.setter
    def width(self, val):
        """Setter function of the width prop"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """Getter function of the height property"""
        return self.__height
    @height.setter
    def height(self, val):
        """Setter function of the height property"""
        print("height set")
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    def area(self):
        """This function returns the area of the rectangle"""
        return self.__width * self.__height
    def perimeter(self):
        """This function returns the perimeter of the rectangle"""
        if width == 0 or height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

