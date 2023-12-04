#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            idx = 0
            while idx < len(i):
                print("{:d}".format(i[idx]), end="")
                if idx < len(i) - 1:
                    print(" ", end="")
                else:
                    print()
                idx += 1
    else:
        print()
