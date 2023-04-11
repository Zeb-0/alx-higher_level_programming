#!/usr/bin/python3

''' adds a new attribute to an object if it’s possible: '''


class Myclass:
    '''creates a class Myclass '''
    pass

''' create instance of Myclass'''
obj = MyClass()
add_attribute(obj, 'new_attribute', 42)
print(obj.new_attribute)  # prints 42
