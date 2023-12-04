#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for i in matrix:
            idx = 0
            while idx < len(i):
                print("{}".format(i[idx]), end ="")
                if idx < len(i) - 1:
                    print(" ", end="")
                else:
                    print()
                idx += 1
