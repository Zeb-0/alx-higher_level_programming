#!/usr/bin/python3

''' defines a module for Rectangle '''

from models.base import Base


class Rectangle(Base):
    ''' rectangle class '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''rectangle instance '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' gets width attribute '''
        return self.__width

    @property
    def height(self):
        ''' gets height value '''
        return self.__height

    @property
    def x(self):
        '''get value of x'''
        return self.__x

    @proprty
    def y(self):
        ''' value of y'''
        return self.__y

    # setter functions
    @heigth.setter
    def height(self, value):
        ''' sets height attribute '''
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be greater than 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """Sets the value for width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be greater than 0")

        self.__width = value


    @x.setter
    def x(self, value):
        ''' sets x value attribute '''
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be greater or equal to 0")
        self.__x = value

    @y.setter
    def y(self, value):
        ''' set y value '''
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' rectangle area '''
        return (self.__width * self.__height)
    def display(self):
        '''display area using '*" in console'''
        for y in range(self.y):
            print('')
        for h in range(self.__height):
            for x in range(self.x):
                print(' ', end='')
            for w in range(self.__width):
                print('*', end='')
            print()

    def __str__(self):
        ''' string repof rectangle '''
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        ''' assign arguments to attributes '''
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        ''' Return dictionary rep of a Rectangle '''

        obj_dictionary = {'id': self.id, 'width': self.__width,
                          'height': self.__height, 'x': self.__x,
                          'y': self.__y}

        return obj_dictionary
