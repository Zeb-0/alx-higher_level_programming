#!/usr/bin/python3
''' defines a class Rectangle '''
from models.base import Base


class Rectangle(Base):
    ''' a class Rectangle '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Initializes Rectangle instance '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    # Property getters
    @property
    def width(self):
        ''' get attribute for width '''
        return self.__width

    @property
    def height(self):
        ''' get attribute for height '''
        return self.__height

    @property
    def x(self):
        ''' get attribute for x '''
        return self.__x

    @property
    def y(self):
        ''' get attribute for y '''
        return self.__y

    # Property setters
    @width.setter
    def width(self, value):
        ''' set value attribute for width '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @height.setter
    def height(self, value):
        ''' set value attribute for height '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @x.setter
    def x(self, value):
        ''' set value attribute for x '''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @y.setter
    def y(self, value):
        ''' set value attribute for y '''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value

    def area(self):
        ''' get rect area '''
        return (self.__width * self.__height)

    def display(self):
        ''' display rectangle using # '''
        for i in range(self.__y):
            print()
        for r in range(self.__height):
            for j in range(self.__x):
                print(' ', end='')
            for col in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        ''''string representation of the class '''
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        ''' assigns arguments to each attribute '''
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        ''' dictionary rep of the rectangle '''
        obj_dict = {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
        return obj_dict
