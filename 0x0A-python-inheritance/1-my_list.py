#!/usr/bin/python3
class MyList(list):
    """
    A sub class of list
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        All elements of the list will be of type int
        """
        sorted_list = sorted(self)
        print(sorted_list)
