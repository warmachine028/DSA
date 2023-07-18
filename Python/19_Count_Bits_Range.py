# CODE 19: Count bits in all numbers in range 0, n + 1

def count_bits(n: int) -> list[int]:
    table = [0] * (n + 1)
    for i in range(1, n + 1):
        table[i] = table[i - 1] + 1 if bool(i & 1) else table[i >> 1]
    
    return table


print(count_bits(9))  # [0, 1, 1, 2, 1, 2, 2, 3, 1, 2]
