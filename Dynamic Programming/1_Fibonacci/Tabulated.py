# CODE 1c: Optimization of Fibonacci problem using tabulation

def fib(n: int) -> int:
    table = [0] * (n + 3)
    table[1] = 1
    for i in range(n):
        table[i + 1] += table[i]
        table[i + 2] += table[i]
    
    return table[n]


print(fib(6))  # 8
print(fib(7))  # 13
print(fib(8))  # 21
print(fib(50))  # 12586269025
