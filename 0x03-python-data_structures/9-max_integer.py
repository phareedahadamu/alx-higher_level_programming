#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    check = my_list[0]
    if len(my_list) > 1:
        for i in range(1, len(my_list)):
            if my_list[i] > check:
                check = my_list[i]
    return (check)
