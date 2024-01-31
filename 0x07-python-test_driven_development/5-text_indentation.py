#!/usr/bin/python3
""" A function that prints a text with 2 new lines after each of these
    characters: ., ? and :"""


def text_indentation(text):
    """Prototype: def text_indentation(text):
    - text must be a string, otherwise raise a TypeError exception with the
    message text must be a string
    - There should be no space at the beginning or at the end of each
    printed line"""

    if not (isinstance(text, str)):
        raise TypeError("text must be a string")
    tmp = 0
    count = 0
    for i in text:
        count += 1
        if (i == '.' or i == '?' or i == ':'):
            print(text[tmp:count])
            print()
            tmp = count
            if (tmp < len(text)):
                while text[tmp] == ' ':
                    tmp += 1
    if tmp < len(text):
        print(text[tmp:count], end="")
