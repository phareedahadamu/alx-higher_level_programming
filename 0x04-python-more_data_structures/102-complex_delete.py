#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for key in a_dictionary:
        if a_dictionary.get(key) == value:
            keys.append(key)
    for i in keys:
        a_dictionary.pop(i)
    return a_dictionary
