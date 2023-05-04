#!/usr/bin/python3
"""In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.

  Prototype: def minOperations(n)
  Returns an integer
  If n is impossible to achieve, return 0

Example:
n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH
=> Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n):
    """Determine the fewest number of operations needed to result in
  exactly n H characters in the file

    Args:
        n (int): an integer number
    Returns:
        an integer
    """
    if n < 2 or not isinstance(n, int):
        return 0

    numOperations = 0
    minOperations = 2
    while minOperations <= n:
        while n % minOperations == 0:
            numOperations += minOperations
            n /= minOperations
        minOperations += 1
    return numOperations
