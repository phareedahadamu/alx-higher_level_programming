#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_list = list(a_dictionary.items())
    my_list.sort()
    for i in my_list:
        print("{}: {}".format(i[0], i[1]))
