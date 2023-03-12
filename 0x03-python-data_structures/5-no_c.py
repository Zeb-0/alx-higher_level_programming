#!/usr/bin/python3
'''  Remove all characters c and C from a string.'''


def no_c(my_string):
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
