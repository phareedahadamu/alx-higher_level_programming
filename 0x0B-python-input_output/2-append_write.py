#!/usr/bin/python3
""" Defines the append_write function"""


def append_write(filename="", text=""):
    """ A function that appends a string at the end of a text file (UTF8) and
    returns the number of characters added. Must use the with statement"""

    with open(filename, 'a', encoding="utf-8") as f:
        count = f.write(text)
    return count
