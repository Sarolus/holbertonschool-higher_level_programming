#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>"), exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    o = sys.argv[2]

    if o == '+':
        summ = add(a, b)
    elif o == '-':
        summ = sub(a, b)
    elif o == '*':
        summ = mul(a, b)
    elif o == '/':
        summ = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /"), exit(1)

    print("{} {} {} = {}".format(a, o, b, summ))
