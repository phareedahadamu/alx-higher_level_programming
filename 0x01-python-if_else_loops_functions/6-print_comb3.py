#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            print("{}{}".format(i, j), end="")
            print("{}".format(", ") if i < 8 else "{}".format("\n"), end="")
