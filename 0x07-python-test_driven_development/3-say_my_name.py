#!/usr/bin/python3

''' module containing a function that prints a name'''


def say_my_name(first_name, last_name=""):
    ''' prints name: <first name> <last name>

    Params:
        first_name: first name of type string
        last_name: last name

    Raises:
        TypeError: if entry is not of type string
        '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
