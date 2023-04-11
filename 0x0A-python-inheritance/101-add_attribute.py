#!/usr/bin/python3

''' adds a new attribute to an object if it’s possible: '''


def add_attributes(obj, attrib, value):
    ''' try adding an attribute to an object '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("not possible")
    obj.__dict__[att] = value
