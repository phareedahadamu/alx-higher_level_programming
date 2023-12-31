#!/usr/bin/python3
def safe_print_integer_err(value):
    check = 0
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as ex:
        check = 1
        print("Exception: {}".format(ex))
    return True if check == 0 else False
