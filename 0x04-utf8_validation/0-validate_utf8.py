#!/usr/bin/python3
"""Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ Define a method to determine a valid UTF-8 encoding
    """
    # 1000 0000
    byte1 = 1 << 7
    # 0100 0000
    byte2 = 1 << 6
    numOfBytes = 0
    if type(data) is not list:
        return False
    if len(data) == 0 or not data:
        return True
    for n in data:
        byte = 1 << 7
        if numOfBytes == 0:
            while (byte & n):
                numOfBytes += 1
                byte = byte >> 1
            if numOfBytes == 0:
                continue
            if numOfBytes == 1 or numOfBytes > 4:
                return False
        else:
            if not (n & byte1 and not (n & byte2)):
                return False
        numOfBytes -= 1
    if numOfBytes:
        return False
    return True
