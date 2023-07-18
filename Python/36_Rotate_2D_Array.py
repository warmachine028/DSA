# CODE 36: Rotate a 2D Array 90 Degrees
"""
1 2 3    1 4 7    7 4 1          m[0][0] = m[0][0]         m[0][0] = m[0][2]
4 5 6 -> 2 5 8 -> 8 5 2    -->   m[0][1] = m[1][0]   -->   m[0][1] = m[0][1]
7 8 9    3 6 9    9 6 3          m[0][2] = m[2][0]         m[0][2] = m[0][0]
                                    Transposing                Reversing


                                    Optimised
                                 m[0][0] = m[2][0]
                                 m[0][1] = m[1][0]
                                 m[0][2] = m[0][0]
"""


# Brute Force
def rotate(matrix: list[list[int]]) -> None:
    aux = [[0]* len(matrix) for _ in matrix] 
    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[i]):
            aux[i][j] = matrix[len(matrix) - j - 1][i]
    
    for i, _ in enumerate(aux):
        for j, item in enumerate(aux[i]):
            matrix[i][j] = item
    


# Optimised
def rotate(matrix: list[list[int]]) -> None:
    # Transposing a matrix
    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[i:], i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reversing array
        matrix[i] = matrix[i][::-1]

ar = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(ar)
print(ar)
