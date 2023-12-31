#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
    return result
