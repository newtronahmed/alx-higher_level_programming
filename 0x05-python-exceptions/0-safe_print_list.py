#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count = count + 1
    except (ValueError, IndexError, TypeError):
        pass
    print()
    return count
