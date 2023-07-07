#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the locked boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = set()
    stack = [0]  # Start with the first box (box 0)

    while stack:
        box = stack.pop()
        visited.add(box)

        for key in boxes[box]:
            if key < n and key not in visited:
                stack.append(key)

    return len(visited) == n
