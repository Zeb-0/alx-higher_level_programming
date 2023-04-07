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

    n = 0  # character count
    while n < len(text) and text[n] == " ":
        n = n + 1

    while n < len(text):
        print(text[n], end="")
        if text[n] == "\n" or text[n] in ".?:":
            if text[n] in ".?:":
                print("\n")
            n = n + 1
            while n < len(text) and text[n] == " ":
                n = n + 1
            continue
        n = n + 1
