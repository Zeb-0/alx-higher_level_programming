#!/usr/bin/python3

''' class square - inherits from Rectangle '''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' A square class inheriting from Rectangle.'''
    def __init__(self, size):
        ''' initialize new square '''

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
