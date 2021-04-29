#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    summ = 0
    summ = sum(int(i) for i in sys.argv[1:])

    print("{}".format(summ))
