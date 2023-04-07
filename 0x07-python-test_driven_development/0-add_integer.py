#!/usr/bin/python3

''' a function that adds 2 integers. '''


def add_integer(a, b=98):
    '''takes two integers or floats and returns their sum

    Params:
        a: input integer
        b: input integer

    Returns:
        sum of the two parameters

    Raises:
        TypeError: if input value is not an integer or a float
    '''

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
