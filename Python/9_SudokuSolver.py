# CODE 9: Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
from string import digits
from typing import List

numbers = [digit for digit in digits][1:]


class Solution:
    solved = False
    
    @staticmethod
    def is_valid(grid, num, row, col):
        if num in grid[row]:
            return False
        
        for i in range(9):
            if num == grid[i][col]:
                return False
        
        box_x = row // 3 * 3
        box_y = col // 3 * 3
        for i in range(box_x, box_x + 3):
            for j in range(box_y, box_y + 3):
                if grid[i][j] == num:
                    return False
        return True
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(10):
            if i == 9:
                self.solved = True
                break
            for j in range(9):
                if board[i][j] != '.':
                    continue
                for num in numbers:
                    if self.is_valid(board, num, i, j):
                        board[i][j] = num
                        self.solveSudoku(board)
                        if self.solved:
                            return
                        board[i][j] = '.'
                return


array = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

Solution().solveSudoku(array)

print(array)
