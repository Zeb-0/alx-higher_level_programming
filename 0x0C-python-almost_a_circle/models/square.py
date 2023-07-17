#!/usr/bin/python3

''' defines class Square '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' class square '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' square instance '''
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' return string rep of square '''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        ''' get value of square size '''
        return self.__width

    @size.setter
    def size(self, value):
        ''' set value for size '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be grater than 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        ''' update square instances's attributes'''
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            elif len(args) > 1:
                self.size = args[1]
            elif len(args) > 2:
                self.x = args[2]
            elif len(args) > 3:
                self.y = args[3]
            else:
                for k, v in kwargs.items():
                    if k == "id":
                        if type(v) != int and v is not None:
                            raise TypeError("id must be an integer")
                        self.id = v
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns dictionary rep of a Square"""

        obj_dictionary = {'id': self.id, 'size': self.size, 'x': self.x,
                          'y': self.y}

        return obj_dictionary
