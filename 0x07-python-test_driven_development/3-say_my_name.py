#!/usr/bin/python3
""" Module say_my_name """


def say_my_name(first_name, last_name=""):
    """
        Takes in first_name and last_name and prints sentence.

        Args:
            first_name (str): first name
            last_name (str): last name
        Returns:
            void
    """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
