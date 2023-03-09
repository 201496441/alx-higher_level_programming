#!/usr/bin/python3

import sys

if __name__ == '__main__':
    args = sys.argv[1:]  # get all arguments except the program name itself
    n_args = len(args)  # count the number of arguments

    # print the number of arguments and the list of arguments
    if n_args == 0:
        print("0 arguments.")
    elif n_args == 1:
        print("1 argument:", args[0])
    else:
        print(n_args, "arguments:", end=" ")
        for i, arg in enumerate(args):
            print(f"\n{i + 1}: {arg}")

