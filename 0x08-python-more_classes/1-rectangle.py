#!/usr/bin/python3

''' define a class Rectangle '''

class Rectangle:
    ''' defines Rectangle by its dimensions  '''

    def __init__(self, with = 0, height = 0):
        ''' initializing instances of Rectangle
        Args:
            width: rectangle width
            height: rectangle height
        Raises:
            ValueError: if width is less than 0
            TypeError: if the size is not of type integer
        '''

        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        retrieve the width attribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' set the width attribute '''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @property
        def height(self):
            ''' method to retrieve the height attribute '''
            return self.__height

        @height.setter
        def height(self, value):
            ''' set the rectangle height attribute '''

            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
