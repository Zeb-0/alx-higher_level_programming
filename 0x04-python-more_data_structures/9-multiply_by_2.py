#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for val in a_dictionary:
        new[val] = a_dictionary[val] * 2
    return new
