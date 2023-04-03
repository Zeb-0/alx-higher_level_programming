#!/usr/bin/python3

'''define a class Rectangle'''

class Rectangle:
    '''rectangle'''
    def __init__(self, width = 0, height = 0):
        '''initialize rectangle instances' dimensions: width and height
        parameters:
            width: retangle width
            height: rectangle height.
        raises:
            TypeError: if the size is not of type integer
            ValueError: if value is less than 0.
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        ''' get the method to retrieve width attribute'''
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
        ''' retrieve the rectangle height attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set the height attribute for rectangle'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

     def area(self):
        '''returns the rectangle area'''
        return (self._Rectangle__width * self._Rectangle__height)

    def perimeter(self):
        '''calculates perimeter and returns result'''
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return 0
        else:
            return 2 * (self._Rectangle__width + self._Rectangle__height)
