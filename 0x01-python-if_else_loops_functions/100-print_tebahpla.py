#!/usr/bin/env python3
for c in reversed(range(ord('a'), ord('z') + 1)):
        if c % 2 != 0:
            c = c - 32
        print("{:c}".format(c), end='')
