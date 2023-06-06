#!/usr/bin/python3
""" The text indentation module"""
def text_indentation(text):
    """
        Takes in text and prints the indented form
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for delim in ".?:":
        text = (delim + "\n\n").join(
                [i.strip(" ") for i in text.split(delim)])
    print("{}".format(text, end=""))
