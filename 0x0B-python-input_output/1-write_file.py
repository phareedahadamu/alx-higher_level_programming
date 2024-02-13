#!/usr/bin/python3
""" Defines the write_file function"""


def write_file(filename="", text=""):
    """ a function that writes a string to a text file (UTF8) and returns
    the number of characters written. must use the with statement"""

    with open(filename, 'w', encoding="utf-8") as f:
        count = f.write(text)
    return count
