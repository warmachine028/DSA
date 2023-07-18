# CODE 34: Reverse a 32 Bit integer
import math

MIN = -2147483648
MAX = +2147483647


def reverse(x: int) -> int:
    res = 0
    while x:
        digit = math.fmod(x, 10)
        res = res * 10 + digit
        x = int(x / 10)
    
    return int(res) if MIN <= res <= MAX else 0


print(reverse(100))  # 1
print(reverse(1))  # 1
print(reverse(199))  # 991
print(reverse(990))  # 99
print(reverse(909))  # 999
print(reverse(0))  # 0
print(reverse(-1))  # -1
print(reverse(-23))  # -32
print(reverse(2147483647))  # -32
print(reverse(-2147483647))  # -32
print(reverse(7463847412))  # -32
print(reverse(-8463847412))  # -32
