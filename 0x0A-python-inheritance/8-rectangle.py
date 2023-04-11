#!/usr/bin/env python3

''' class Rectangle - inherits from BaseGeometry '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    ''' rectangle inheriting from BaseGeometry. '''

    def __init__(self, width, height):
        ''' Initialize a new rectangle instance.'''
        self.__width = width
        self.__height = height
        super().__init__()

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Compute the area of the rectangle."""
        return self.__width * self.__height

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
