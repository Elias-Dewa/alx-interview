#!/usr/bin/python3
"""Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ Define a method to determine a valid UTF-8 encoding
    """
    if type(data) is not list:
        return False
    if len(data) == 0 or not data:
        return True
    if len(data) == 1:
        if data[0] >= 32 and data[0] <= 126:
            return True
        else:
            return False
    for n in data:
        if type(n) is not int:
            return False
        if n > 31 and n < 127:
            continue
        elif n == 0:
            continue
        else:
            return False
    return True
