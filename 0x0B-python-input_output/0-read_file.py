#!/usr/bin/bash

'''  reads a text file (UTF8) and prints it to stdout: '''


def read_file(filename=""):
    ''' it returns contents of UTF8 text file '''
    with open(filename, encoding='utf-8') as fname:
        print(fname.read(), end='')
