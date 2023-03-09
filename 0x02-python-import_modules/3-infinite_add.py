#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv[1:]  # get all arguments except the program name itself
    total = sum(int(arg) for arg in args)  # convert each argument to int and sum them
    print(total)

