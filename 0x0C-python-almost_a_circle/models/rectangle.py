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
    # property getter funcs

    @property
    def height(self):
        ''' get attribute for height '''
        return self.__height

    @property
    def width(self):
        ''' get attribute for width '''
        return self.__width

    @property
    def x(self):
        ''' get attribute for x '''
        return self.__x

    @property
    def y(self):
        ''' get attribute for y '''
        return self.__y

    # setter funcs

    @height.setter
    def height(self, value):
        ''' set value attribute for height '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @width.setter
    def width(self, value):
        ''' set value attribute for width '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @x.setter
    def x(self, value):
        ''' set value attribute for x '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value <= 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @y.setter
    def y(self, value):
        ''' set value attribute for y '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value <= 0:
            raise ValueError('y must be >= 0')

        self.__y = value

    def area(self):
        ''' get rect area '''
        return (self.__width * self.__height)

    def display(self):
        ''' display rectangle using # '''
        for i in range(self.__y):
            print('')
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
        if args and len(args) != 0:
            ag = 0
            for i in args:  # i reps an argument
                if ag == 0:
                    if i is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = i
                elif ag == 1:
                    self.width = i
                elif ag == 2:
                    self.height = i
                elif ag == 3:
                    self.x = i
                elif ag == 4:
                    self.y = i
                ag += 1

            if kwargs:
                for key, value in kwargs.items():
                    if key == 'id':
                        if value is None:
                            self.__init__(self.width,
                                          self.height,
                                          self.x,
                                          self.y)
                        else:
                            self.id = value
                    elif key == 'width':
                        self.width = value
                    elif key == 'height':
                        self.height = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value

    def to_dictionary(self):
        ''' dictionary rep of the rectangle '''
        obj_dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return obj_dict
