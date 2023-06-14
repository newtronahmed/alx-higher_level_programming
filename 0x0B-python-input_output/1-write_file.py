#!/usr/bin/python3
"""This module contains write fule function"""


def write_file(filename="", text=""):
    """ Writes to file and returns num chars"""
    with open(filename, mode="w", encoding="utf-8") as f:
        bytes_written = f.write(text)
        return bytes_written
