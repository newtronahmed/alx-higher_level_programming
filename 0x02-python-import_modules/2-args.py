#!/usr/bin/python3
import sys
if __name__ == '__main__':
    print("{} argument{}".format(len(sys.argv) - 1, "s" if len(sys.argv) != 2 else ""))
    for i in range(len(sys.argv)):
        if i != 0:
            print("{}: {}".format(i, sys.argv[i]))
