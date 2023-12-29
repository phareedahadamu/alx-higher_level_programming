#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total = 0
    num = 0
    result = 0
    for i in my_list:
        total += (i[0] * i[1])
        num += i[1]
    result = total / num
    return result
