from functools import lru_cache


def findFibonacci(n: int) -> int:
    if n < 0:
        raise ValueError
    if n <= 1:
        return n

    fib_numbers = [0, 1]

    for i in range(2, n + 1):
        fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]

    return fib_numbers[n]


@lru_cache(3)
def findFibonacciRecursive(n: int) -> int:
    if n <= 2:
        return 1

    return findFibonacciRecursive(n - 1) + findFibonacciRecursive(n - 2)
