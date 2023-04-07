#!/usr/bin/python3

''' indennts text '''


def text_indentation(text):
    '''prints 2lines of text after "., ? and :"

    Params:
        text: input string

    Raise:
        TypeError: if text is not of type string
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    else:
        for char in text:
            if char == '.' or char =='?' or char == ':':
                print()
                print(char)
                print()
            else:
                print(char, end='')
