#!/usr/bin/python3

''' class Rectangle - inherits from BaseGeometry '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    ''' rectangle inheriting from BaseGeometry. '''

    def __init__(self, width, height):
        """Initialize a new rectangle instance."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
