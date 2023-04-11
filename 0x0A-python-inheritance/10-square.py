#!/usr/bin/python3

''' class `Square` that inherits from `Rectangle` '''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' A square class inheriting from Rectangle. '''
    def __init__(self, size):
        """Initialize a new square instance."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
