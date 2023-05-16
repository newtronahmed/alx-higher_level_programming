#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return_array = []
    for i in my_list:
        if (i % 2) == 0:
            return_array.append(True)
        else:
            return_array.append(False)
    return return_array
