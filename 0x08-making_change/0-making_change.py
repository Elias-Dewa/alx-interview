#!/usr/bin/env python3
"""Determine the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """Make a change to a given amount of coins"""
    if total < 1:
        return 0
    coinsChange = 0
    coins.sort()
    coins.reverse()
    for i in coins:
        change = int(total / i)
        total -= change * i
        coinsChange += change
        if total == 0:
            return coinsChange
    if total != 0:
        return -1
