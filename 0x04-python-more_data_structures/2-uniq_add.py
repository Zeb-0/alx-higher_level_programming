#!/usr/bin/python3
def uniq_add(my_list=[]):
    setlist = set(my_list)
    x = 0
    for i in setlist:
        x += i
    return x
