#!/usr/bin/python3
for num1 in range(10):
    for num2 in range(10):
        if num1 == num2 or num1 > num2:
            pass
        else:
            print("{}{}".format(num1, num2), end=", " if not (num1 == 8 and num2 == 9) else "\n")
