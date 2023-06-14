#!/usr/bin/python3
import json
"""This module contains load from json file function"""


def load_from_json_file(filename):
    with open(filename, mode="r", encoding="utf-8") as f:
        text = f.read()
    return json.loads(text)
