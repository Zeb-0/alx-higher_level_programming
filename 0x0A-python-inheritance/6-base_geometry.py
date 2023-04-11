#!/usr/bin/python3
''' Empty class BaseGeometry '''


class BaseGeometry:
    """
    BaseGeometry class with the area() method that raises an exception.
    """
    def area(self):
        """
        Raises an Exception.
        """
        raise Exception('area() is not implemented')
