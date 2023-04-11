#!/usr/bin/python3

''' check if object is an instance of a class
that inherited from a specified class'''


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified class or
    if the object is an instance of a class that inherited from the specified class;
    otherwise False.
    """
    return isinstance(obj, a_class)
