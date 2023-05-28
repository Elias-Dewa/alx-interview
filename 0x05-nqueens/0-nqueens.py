#!/usr/bin/env python3
"""A program that solves the N queens problem"""


import sys


def nqueens(N, k, board):
    """a method that solves the N queens problem"""
    for i in range(N):
        isController = False
        for j in board:
            if (i == j[1]) or (i - j[1] == j[0] - k) or (k - i == j[0] - j[1]):
                isController = True
        if not isController:
            board.append([k, i])
            if (N - 1) != k:
                nqueens(N, k + 1, board)
            else:
                print(board)
            del board[-1]


if __name__ == "__main__":
    """main"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)
    nqueens(int(sys.argv[1]), 0, [])
