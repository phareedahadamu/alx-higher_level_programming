#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list2 = []
    for i in my_list:
        if i == search:
            i = replace
        list2.append(i)
    return list2
