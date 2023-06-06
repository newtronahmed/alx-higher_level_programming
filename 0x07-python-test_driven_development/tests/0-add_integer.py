#!/usr/bin/python3
""" This module contains the function add_integer."""
def add_integer(a, b=98):
   """ This function adds tow integers
        
        Parameters:
            a (int): decimal or float parameter
            b (int): decimal or float parameter

        Returns:
            results (int): sum of a and b

>>> add_integer = __import__("0-add_integer").add_integer

run tests:

>>> add_integer(10, 11)
21

>>> add_integer(10, 11.5)
21

>>> add_integer(15, 'a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/root/alx-higher_level_programming/0x07-python-test_driven_development/0-add_integer.py", line 16, in add_integer
    raise TypeError("b must be an integer")
TypeError: b must be an integer

>>> add_integer()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add_integer() missing 1 required positional argument: 'a'

>>> add_integer(-1, -1)
-2

>>> add_integer(-1, 1)
0

>>> add_integer(None)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/root/alx-higher_level_programming/0x07-python-test_driven_development/0-add_integer.py", line 14, in add_integer
    raise TypeError("a must be an integer")
TypeError: a must be an integer

>>> add_integer(float("nan"))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/root/alx-higher_level_programming/0x07-python-test_driven_development/0-add_integer.py", line 18, in add_integer
    a= int(a)
ValueError: cannot convert float NaN to integer

>>> add_integer(1000e1000)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/root/alx-higher_level_programming/0x07-python-test_driven_development/0-add_integer.py", line 18, in add_integer
    a= int(a)
OverflowError: cannot convert float infinity to integer
   """
   if not isinstance(a, (int, float)):
       raise TypeError("a must be an integer")
   if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
   if isinstance(a, float):
        a= int(a)
   if isinstance(b, float):
        b= int(b)
   results = a + b
   return results
