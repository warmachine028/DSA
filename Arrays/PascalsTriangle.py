from math import factorial


class PascalsTriangle:
    @staticmethod
    def generateTriangle(columns: int) -> list[list[int]]:  # Brute Force
        result = [[1]]
        for col in range(2, columns):
            temp = []
            for row in range(col):
                item = 1 if row in (0, col - 1) else sum(result[-1][row - 1 : row + 1])
                temp.append(item)
            result.append(temp)
        return result

    @staticmethod
    def generateTriangle1(columns: int) -> list[list[int]]:
        result = []
        for col in range(1, columns):
            temp = [1]
            for row in range(1, col):
                temp.append(int(temp[row - 1] * (col - row) / row))
            result.append(temp)
        return result

    @staticmethod
    def generateRow(rows: int) -> list[int]:  # T => O(r), S => O(r)
        result = [1]
        for i in range(1, rows):
            result.append(int(result[i - 1] * (rows - i) / i))
        return result

    @staticmethod
    def generateItem(
        row: int, column: int
    ) -> int:  # nCR => BruteForce T -> O(r) + O(c) + O(r - c)
        result = factorial(row - 1) / (factorial(column - 1) * factorial(row - column))
        return int(result)

    @staticmethod
    def generateItem1(
        row: int, column: int
    ) -> int:  # nCR => Optimised T -> O(r), S -> O(1)
        row -= 1
        column -= 1
        result = 1
        for i in range(column):
            result *= row - i
            result /= i + 1
        return int(result)


print(PascalsTriangle.generateItem(5, 3))
print(PascalsTriangle.generateItem1(5, 3))
print(PascalsTriangle.generateRow(6))
for i in range(10):
    print(PascalsTriangle.generateRow(i))
print()
print(*PascalsTriangle.generateTriangle(10), sep="\n")
