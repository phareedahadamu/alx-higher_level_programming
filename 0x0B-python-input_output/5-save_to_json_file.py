#!/usr/bin/python3
""" Defines the save_to_json_file(my_obj, filename) function"""


def save_to_json_file(my_obj, filename):
    """ A function that writes an Object to a text file, using a JSON
    representation"""

    import json
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
