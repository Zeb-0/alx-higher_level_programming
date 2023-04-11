#!/usr/bin/python3

''' object instance of a class that inherited (directlyorindirectly) from class'''


def inherits_from(obj, a_class):
    ''' 
    Return True if object is inctance f a class that inherited
    (directly or indirectly) from the specified class; otherwise False.
    '''
    return isinstance(obj, type) and issubclass(obj, a_class) and obj is not a_class
