#!/usr/bin/python3
"""This module contains load from json file function"""

import json


def load_from_json_file(filename):
    with open(filename, mode="r", encoding="utf-8") as f:
        text = f.read()
    return json.loads(text)
