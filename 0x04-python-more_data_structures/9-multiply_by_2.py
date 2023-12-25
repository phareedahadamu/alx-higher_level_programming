#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = {}
    d = a_dictionary.copy()
    for key in d:
        d[key] = d.get(key) * 2
    return d
