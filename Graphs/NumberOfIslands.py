from typing import List

class Solution:
    def markIsland(self, row, column, grid):
        pass

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                # if not visited
                if grid[r][c] == '1':
                    self.markIsland(r, c, grid)
                    islands += 1
        return islands