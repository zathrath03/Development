# 4.18 µs ± 24.5 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
def fib(n: int) -> int:        
    if n <= 1:
        return n

    sequence = [0, 1]

    for _ in range(n-1):
        sequence.append(sum(sequence[-2:]))

    return sequence[n]

# 2.33 µs ± 10.3 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
def fib2(N: int) -> int:
    if N <= 1:
        return N
    
    cache = [0] * (N + 1)
    cache[1] = 1
    for i in range(2, N + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[N]

# 72.5 ns ± 0.328 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
cache = {0: 0, 1: 1}
def fib3(N: int) -> int:
    if N in cache:
        return cache[N]
    cache[N] = fib3(N - 1) + fib3(N - 2)
    return cache[N]

# 976 ns ± 14.5 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
def fib4(N: int) -> int:
    if (N <= 1):
        return N

    current = 0
    prev1 = 1
    prev2 = 0

    for i in range(2, N + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return current

# 201 ns ± 5.96 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
def fib6(N: int) -> int:
        return int(round((((1 + (5 ** 0.5)) / 2) ** N) / (5 ** 0.5)))