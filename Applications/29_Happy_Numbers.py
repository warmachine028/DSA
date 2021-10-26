# CODE 29: Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not
# include 1. Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Recursive
def isHappy(n: int, memo=None) -> bool:
    if memo is None:
        memo = {}
    if n == 1:
        return True
    if n in memo:
        return False
    
    x = 0
    temp = n
    while temp:
        res = divmod(temp, 10)
        temp = res[0]
        x += res[1] ** 2
    memo[n] = x
    return isHappy(x, memo)


# Iterative
def is_happy(n: int):
    table = []
    while n != 1:
        n = sum(int(digit) ** 2 for digit in str(n))
        if n in table: return False
        table.append(n)
    return True


print(isHappy(2))  # False
print(isHappy(7))  # True
print(isHappy(19))  # True
print(isHappy(2147483647))  # False
print(isHappy(990))  # False
print()
print(is_happy(2))  # False
print(is_happy(7))  # True
print(is_happy(19))  # True
print(is_happy(2147483647))  # False
print(is_happy(990))  # False
