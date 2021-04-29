#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    summ = 0
    args = len(sys.argv)

    for i in range(1, args):
        summ += int(sys.argv[i])
    print("{}".format(summ))
