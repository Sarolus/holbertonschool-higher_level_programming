#!/usr/bin/python3
for i in range(9):
    for j in range(i +1, 10):
        if (i < j):
            print("{:d}{:d}".format(i, j), end='')
        if (i < 8):
            print(", ", end="")
print("\n", end= "")
