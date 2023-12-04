#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("{0}".format("\n"), end="")
    else:
        for i in matrix:
            idx = 0
            while idx < len(i):
                print("{:d}".format(i[idx]), end="")
                if idx < len(i) - 1:
                    print(" ", end="")
                idx += 1
            print()
