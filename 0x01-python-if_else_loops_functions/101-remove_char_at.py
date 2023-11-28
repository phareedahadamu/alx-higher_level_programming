#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    i = 0
    str2 = ""
    while i < length:
        if i == n:
            i += 1
            continue
        str2 = str2 + str[i]
        i += 1
    return (str2)
