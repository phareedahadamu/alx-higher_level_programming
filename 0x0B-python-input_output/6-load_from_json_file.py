#!/usr/bin/python3
""" Defines the load_from_json_file(filename) function"""


def load_from_json_file(filename):
    """ A function that creates an Object from a “JSON file”. Must use
    with statement"""
    import json
    with open(filename, 'r', encoding="utf-8") as f:
        my_obj = json.load(f)
    return my_obj
