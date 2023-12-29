#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if isinstance(roman_string, str) is not True or roman_string is None:
        return 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    while i < len(roman_string) - 1:
        if d.get(roman_string[i]) < d.get(roman_string[i + 1]):
            result += (d.get(roman_string[i + 1]) - d.get(roman_string[i]))
            i += 2
        else:
            result += d.get(roman_string[i])
            i += 1
    if i < len(roman_string):
        result += d.get(roman_string[i])
    return result
