#!/usr/bin/python3
import numpy as np

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def possible(r, c, n):
    global grid
    for i in range(0, 9):
        if grid[r][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][c] == n:
            return False
    r0 = (r // 3) * 3
    c0 = (c // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[r0+i][c0+j] == n:
                return False
    return True


def solve():
    global grid
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for n in range(1, 10):
                    if possible(r, c, n):
                        grid[r][c] = n
                        solve()
                        grid[r][c] = 0
                return
    print(np.matrix(grid))


solve()
