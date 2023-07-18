from sys import maxsize


def helper(grid, i, j):
    if j == m:
        return maxsize
    if i == n:
        return maxsize
    if i == n - 1 and j == m - 1:
        return
    
    right = helper(grid, i + 1, j)
    down = helper(grid, i, j + 1)
    diagonal = helper(grid, i + 1, j + 1)
    
    return min(right, down, diagonal) + grid[i][j]
