#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for i in matrix:
            for j in i:
                print("{:d}".format(j), end="")
                print("{0}".format("\n") if j == i[len(i) - 1] else "{0}".format(" "), end="") 
           # idx = 0
           # while idx < len(i):
            #    print("{:d}".format(i[idx]), end="")
             #   if idx < len(i) - 1:
              #      print(" ", end="")
               # else:
                #    print()
               # idx += 1
