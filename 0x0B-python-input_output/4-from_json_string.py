#!/usr/bin/python3
""" Defines from_json_string function"""


def from_json_string(my_str):
    """ A function that returns an object (Python data structure) represented
    by a JSON string"""

    import json
    return (json.loads(my_str))
