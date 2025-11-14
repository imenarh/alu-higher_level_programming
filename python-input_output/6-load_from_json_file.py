#!/usr/bin/python3
"""Load from JSON file"""


import json


def load_from_json_file(filename):
    """load from JSON file"""
    with open(filename, "r") as f:
        return json.load(f)
