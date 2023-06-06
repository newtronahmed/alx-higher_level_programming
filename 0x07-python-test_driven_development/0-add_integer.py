#!/usr/bin/python3
""" This module contains the function add_integer."""
def add_integer(a, b=98):
   """ This function adds tow integers
        
        Parameters:
            a (int): decimal or float parameter
            b (int): decimal or float parameter

        Returns:
            results (int): sum of a and b
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
