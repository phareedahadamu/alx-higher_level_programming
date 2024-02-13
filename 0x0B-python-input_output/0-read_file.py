#!/usr/bin/python3
""" Defines the read_file function"""


def read_file(filename=""):
    """ A function that reads a text file (UTF8) and prints it to stdout
    using the with statement"""

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
