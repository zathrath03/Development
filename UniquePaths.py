import math

# 247 ns ± 1.85 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
cache = {}
def MYuniquePaths(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1
    
    uniquePaths = cache.get((m,n), cache.get((n,m)))
    if uniquePaths:
        return uniquePaths
    if m == n:
        uniquePaths = 2 * cache.get((m-1,n), cache.get((m,n-1), 0))
        if uniquePaths:
            cache[(m,n)] = uniquePaths
            return uniquePaths
    
    cache[(m,n)] = MYuniquePaths(m-1, n) + MYuniquePaths(m, n-1)
    return cache[(m,n)]

# 697 µs ± 1.99 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
def uniquePaths2(m: int, n: int) -> int:
    if n > m:
        n, m = m, n
    dp = [1] * n
    for _ in range(1, m):
        for i in range(1, n):
            dp[i] += dp[i-1]
    return dp[-1]

# 10.2 µs ± 32.3 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
def uniquePaths3(m: int, n: int) -> int:
    return math.comb(m + n - 2, n - 1)

# 10.3 µs ± 12.5 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
def uniquePaths31(m: int, n: int) -> int:
    return math.comb(m + n - 2, min(m,n) - 1)