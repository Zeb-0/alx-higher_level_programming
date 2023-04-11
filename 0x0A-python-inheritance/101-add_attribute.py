#!/usr/bin/python3
'''adds new attributes to objects if possible '''


def add_attribute(obj, att, value):
    ''' try to Add a new attribute to an object '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[att] = value
