#!/usr/bin/python3

''' define a class Rectangle '''

class Rectangle:
    '''rectangle'''
    def __init__(self, width = 0, height = 0):
        '''initialize the rectangle instances

        Parameters:
            width(int): rectangle width
            height(int): rectangle height

        Raises:
            TypeError: if type entered is not integer
            ValueError: if value entered is less than 0
        '''

        self.width = width
        self.height = height

    @property
    def width(self):
        ''' retrieve the Rectangle's width '''
        return self.__width

    @width.setter
    def width(self, value):
        '''set the width attribute'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get heighgt of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value)!= int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''calculate area of rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''calculate rectangle perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        '''returns a printable representation of rectangle using '#' '''

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    rectangle += "#"
                rectangle += "\n"
            return rectangle[:-1]

    def __repr__(self):
        '''return string rep of rectangle'''
        return 'Rectangle({}, {})'.format(self.width, self.height)
