#!/usr/bin/python3

''' checks for instance of a class '''


def is_same_class(obj, a_class):
    '''
    returns true or false if match or doesn't respectively
    '''
    if type(obj) is a_class:
        return True
    else:
        return False
