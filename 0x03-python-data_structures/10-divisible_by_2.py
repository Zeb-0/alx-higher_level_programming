#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    mul_two = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            mul_two[count] = True
        else:
            mul_two[count] = False
    return(mul_two)
