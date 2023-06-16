#!/usr/bin/python3
"""This module contains a function to save to json"""

import json 


def save_to_json_file(my_obj, filename):
    """ This function saves obj to file in json format"""
    obj_string = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(obj_string)
