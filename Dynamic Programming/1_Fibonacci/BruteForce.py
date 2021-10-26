# CODE 1a: Code to get nth fibonacci number

def fib(n: int) -> int:
    return 1 if n <= 2 else fib(n - 1) + fib(n - 2)


print(fib(6))  # 8
print(fib(7))  # 13
print(fib(8))  # 21
print(fib(50))  # 12586269025
