#!/usr/bin/python3

''' class `Square` that inherits from `Rectangle` '''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' A square class inheriting from Rectangle. '''
    def __init__(self, size):
        """Initialize a new square instance."""
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2
