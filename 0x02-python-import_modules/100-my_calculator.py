#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    op = sys.argv[2]
    if op == '+' or op == '-' or op == '*' or op == '/':
        if op == '+':
            result = add(int(sys.argv[1]), int(sys.argv[3]))
        elif op == '-':
            result = sub(int(sys.argv[1]), int(sys.argv[3]))
        elif op == '*':
            result = mul(int(sys.argv[1]), int(sys.argv[3]))
        elif op == '/':
            result = div(int(sys.argv[1]), int(sys.argv[3]))
        print("{} {} {} = {}".format(sys.argv[1], op, sys.argv[3], result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
