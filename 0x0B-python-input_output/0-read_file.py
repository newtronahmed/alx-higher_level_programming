#!/usr/bin/python3
"""This module contains read_file function"""


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print("{}".format(f.read()), end="")
