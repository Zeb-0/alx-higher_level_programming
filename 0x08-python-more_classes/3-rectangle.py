#!/usr/bin/python3
'''class Rectangle '''

class Rectangle:
    '''create instances of Rectangle'''

    def __init__(self, width = 0, height = 0):
        '''initialize Rectangle

        Parameters:
            width: rectangle width
            height: rectangle height
        Raises:
            TypeError: if the type of size is not integer
            ValueError: if value entered is less than 0
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        ''' getter to retrieve the width attribute '''
        return self.__width

    @width.setter
    def width(self, value):
        '''set the width attribute'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''get the height attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set the height'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''calculates area of rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''return the perimeter of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
    def __str__(self):
        '''returns a string representation of rectangle
        using '#' fot its outline
        '''
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for i in range(self.__height):
            rectangle += "#" * self.__width + "\n"
        return rectangle[:-1]
