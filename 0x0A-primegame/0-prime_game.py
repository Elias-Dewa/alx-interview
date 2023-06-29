#!/usr/bin/python3
"""Prime game"""


def primeNumber(i):
    """a method that returns a number, which can be a winner,
    from each game"""
    if (i < 1):
        return None
    if (i == 1):
        return (2)
    nums = list(range(i + 1))
    ply1 = 1
    prime = 2
    prime_lst = []
    for num in nums:
        if (num % prime == 0):
            nums.remove(num)
    prime_lst.append(prime)
    prime = 3
    while (nums != [1]):
        if (ply1 == 1):
            ply1 = 2
        else:
            ply1 = 1
        for num in nums:
            if (num % prime == 0):
                nums.remove(num)
        prime_lst.append(prime)
        prime += 2
        flag = 1
        while (flag):
            for num in prime_lst:
                if (prime % num == 0):
                    prime += 2
                    break
            else:
                flag = 0
    if (ply1 == 1):
        return 1
    return 2


def isWinner(x, nums):
    """a method to determine who the winner of each game"""
    if (x < 1 or x != len(nums)):
        return None

    Maria = 0
    Ben = 0
    for i in nums:
        prime = primeNumber(i)
        if prime == 1:
            Maria += 1
        elif prime == 2:
            Ben += 1
    if Maria == Ben:
        return None
    elif Maria > Ben:
        return "Maria"
    return "Ben"
