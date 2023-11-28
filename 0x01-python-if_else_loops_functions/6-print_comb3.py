#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            print(f"{i}{j}", end="")
            print(f", "if i < 8 else "\n", end="")
