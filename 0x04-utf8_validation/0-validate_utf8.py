#!/usr/bin/python3
"""Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ Define a method to determine a valid UTF-8 encoding
    """
    if len(data) == 0:
        return True
    if type(data) is not list:
        return False
    for n in data:
        if type(n) is not int:
            return False
    return True
