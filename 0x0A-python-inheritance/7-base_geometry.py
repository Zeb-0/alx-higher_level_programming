#!/usr/bin/python3

''' create empty class BaseGeometry'''


class BaseGeometry:
    """
    BaseGeometry class with the area() method that raises an exception.
    """
    def area(self):
        """
        Raises an Exception.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        ''' public instance method that validates value '''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
