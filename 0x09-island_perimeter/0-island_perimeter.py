#!/usr/bin/python3
"""a function that returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """a function that returns the perimeter of the island described in grid"""
    if not grid:
        return 0

    perimeter = 0

    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i]:
                if not j or not grid[j - 1][i]:
                    perimeter += 1
                if not i or not grid[j][i - 1]:
                    perimeter += 1
                if j == len(grid) - 1 or not grid[j + 1][i]:
                    perimeter += 1
                if i == len(grid[0]) - 1 or not grid[j][i + 1]:
                    perimeter += 1
    return perimeter
