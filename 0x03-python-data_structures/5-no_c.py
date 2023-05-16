#!/usr/bin/python3
def no_c(my_string):
    x = list(my_string)
    a = []

    for i in x:
        if i.casefold() != 'C'.casefold():
            a.append(i)
    return ("".join(a))
