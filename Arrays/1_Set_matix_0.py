"""
Set Matrix Zero
Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = range(len(matrix)), range(len(matrix[0]))
        r, c = [], []

        for i in rows:
            for j in cols:
                if matrix[i][j]: continue
                r.append(i)
                c.append(j)
        

        for i in rows:
            for j in cols:
                if i in r or j in c:
                    matrix[i][j] = 0



    "brute Force"
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        rows, cols = range(len(matrix)), range(len(matrix[0]))

        for i in rows:
            for j in cols:
                if matrix[i][j]:
                    continue
                for k in rows:
                    matrix[k][j] = "x" if matrix[k][j] else 0
                for k in cols:
                    matrix[i][k] = "x" if matrix[i][k] else 0

        for i in rows:
            for j in cols:
                if matrix[i][j] == "x":
                    matrix[i][j] = 0
