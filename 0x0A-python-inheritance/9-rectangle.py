#!/usr/bin/python3

''' Class rextangle that inherits from BaseGeometry '''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' rectangle inheriting from BaseGeometry. '''

    def __init__(self, width, height):
        """Initialize a new rectangle instance."""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        ''' computes and returns area of rectangle '''
        return (self.__width * self.__height)

    def __str__(self):
        '''Return a string representation of the rectangle.'''
        return f"[Rectangle] {self.__width}/{self.__height}"
