#!/usr/bin/python3
def safe_print_integer(value):
    check = 0
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        check = 1
    return True if check == 0 else False
