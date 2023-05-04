#!/usr/bin/env python3
"""You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

  Prototype: def canUnlockAll(boxes)
  boxes is a list of lists
  A key with the same number as a box opens that box
  You can assume all keys will be positive integers
  There can be keys that do not have boxes
  The first box boxes[0] is unlocked
  Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened

    Args:
        boxes (list): a list of boxes

    Returns:
        True if all boxes can be opened, else return False
    """
    if len(boxes) == 0:
        return False
    numBoxes = len(boxes)
    unlockedBox = [0]
    for i in unlockedBox:
        for j in boxes[i]:
            if j not in unlockedBox:
                if j < numBoxes and numBoxes != i:
                    unlockedBox.append(j)
    if len(unlockedBox) == numBoxes:
        return True
    return False
