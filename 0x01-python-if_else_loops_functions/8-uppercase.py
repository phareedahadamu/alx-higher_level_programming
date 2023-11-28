#!/usr/bin/python3
def uppercase(str):
    count = 0
    length = len(str)
    for i in range(0, length):
        print("{}".format(chr(ord(str[count]) - 32)) if ord(str[count]) >= 97
              and ord(str[count]) <= 122 else "{}".format(str[count]), end="")
        count += 1
    print("{0}".format("\n"), end="")
