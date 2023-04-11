#!/usr/bin/python3
''' MyInt - inherits from int '''


class MyInt(int):
    ''' Invert int operators == and != '''

    def __eq__(self, other):
        ''' inverts the == and != operators '''
        return self.real != other

    def __ne__(self, other):
        """Override != operator with == behavior"""
        return self.real == other
