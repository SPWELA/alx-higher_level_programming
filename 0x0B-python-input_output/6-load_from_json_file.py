#!/usr/bin/python3
"""JSON TASK 6"""

import json


def load_from_json_file(filename):
    """Creates an Object from a `JSON file`"""
    obj = None
    with open(filename, "r", encoding="utf-8") as f:
        obj = json.load(f)

    return obj
