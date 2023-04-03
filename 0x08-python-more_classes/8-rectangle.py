#!/usr/bin/python3

'''Write a class Rectangle that defines a rectangle'''


class Rectangle:
    '''rep the class Rectangle

    Attributes:
        number_of_instances: number of rectangle instances
        print_symbol: symbol to rep rectangle string format
    '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        ''' initialize instances of Rectangle
         Parameters:
            width(int): rectangle width
            height(int): rectangle height
        Raises:
            TypeError: if type entered is not integer
            ValueError: if value entered is less than 0
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Get height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''returns the biggest rectangle based on area

        Params:
            rect_1 (Rectangle): instance of Rectangle
            rect_2 (Rectangle): instance of Rectangle

        Returns:
            Rectangle: rectangle instance with the biggest area
        '''

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        '''returns a printable representation of rectangle using '#' '''

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        '''return string rep of rectangle'''
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        '''print message on instance deletion'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
