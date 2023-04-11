#!/usr/bin/python3

''' Defines Mylist class inheritor '''


class MyList(list):
    '''
    subclass of list
    '''
    def print_sorted(self):
        '''prints list in ascending order
        '''
        sorted_list = sorted(self)
        print(sorted_list)
