#!/usr/bin/python3
"""This module contains the Rectangle class"""


class Rectangle:
    """This is the rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            for i in range(self.__width):
                rect += type(self).print_symbol 
            rect += "\n"
        return rect[:-1]
    
    def __repr__(self):
        return f"Rectangle({self.__width},{self.__height})"

    def __del__(self): """Called when del is detected"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the biggest Rectangle based on the area
        Args:
            rect_1: Rectangle instance
            rect_2: Rectangle instance different from rect_1
        Returns:
            The instance with the biggest area,
            or rect_1 if both rectangles have the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with width == height == size
        Args:
            size: size to set the new rectangle to
        Returns:
            The new Rectangle instance
        """
        return cls(size, size)
