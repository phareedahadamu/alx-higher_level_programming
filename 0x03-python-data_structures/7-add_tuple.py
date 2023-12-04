#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a)
    b_len = len(tuple_b)
    if a_len >= 2:
        a0 = tuple_a[0]
        a1 = tuple_a[1]
    elif a_len == 1:
        a0 = tuple_a[0]
        a1 = 0
    else:
        a0 = 0
        a1 = 0
    if b_len >= 2:
        b0 = tuple_b[0]
        b1 = tuple_b[1]
    elif b_len == 1:
        b0 = tuple_b[0]
        b1 = 0
    else:
        b0 = 0
        b1 = 0
    new_tuple = ((a0 + b0), (a1 + b1))
    return (new_tuple)
