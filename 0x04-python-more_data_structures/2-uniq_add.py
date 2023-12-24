#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for i in my_list:
        if my_list.count(i) > 1:
            j = 1
            while j < my_list.count(i):
                my_list.remove(i)
                j = j + 1
    for k in my_list:
        total += k
    return total
