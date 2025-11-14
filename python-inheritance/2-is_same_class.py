#!/usr/bin/python3
"""Module that defines a function to check the exact class
of an object."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class.
    Otherwise False."""
    return type(obj) is a_class
