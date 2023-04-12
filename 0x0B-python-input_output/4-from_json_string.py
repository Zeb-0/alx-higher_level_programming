#!/usr/bin/python3

''' defines a n object rep by a JSON string '''
import json


def from_json_string(my_str):
    ''' defines a n object rep by a JSON string '''
    return json.loads(my_str)
