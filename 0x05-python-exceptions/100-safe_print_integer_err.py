#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    check = 0
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as ex:
        check = 1
        print("Exception: {}".format(ex), file=sys.stderr)
    return True if check == 0 else False
