#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        tmp = 0
        for key in a_dictionary:
            tmp = a_dictionary.get(key)
            break
        for keys in a_dictionary:
            if a_dictionary.get(keys) > tmp:
                tmp = a_dictionary.get(keys)
            else:
                continue
        for keyz in a_dictionary:
            if a_dictionary.get(keyz) == tmp:
                break
        return keyz
