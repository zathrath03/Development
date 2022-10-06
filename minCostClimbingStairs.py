from functools import cache
import random

# 217 µs ± 665 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
def MYminCostClimbingStairs(cost: list[int]) -> int:
    if len(cost) == 2:
        return min(cost)
    cache = {0: cost[0], 1: cost[1]}
    for i in range(2, len(cost)):
        cache[i] = cost[i] + min(cache[i-1], cache[i-2])
        
    return min(cache[len(cost)-1], cache[len(cost)-2])

# 248 µs ± 9.55 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
def minCostClimbingStairs1(cost: list[int]) -> int:
    # The array's length should be 1 longer than the length of cost
    # This is because we can treat the "top floor" as a step to reach
    minimum_cost = [0] * (len(cost) + 1)
    
    # Start iteration from step 2, since the minimum cost of reaching
    # step 0 and step 1 is 0
    for i in range(2, len(cost) + 1):
        take_one_step = minimum_cost[i - 1] + cost[i - 1]
        take_two_steps = minimum_cost[i - 2] + cost[i - 2]
        minimum_cost[i] = min(take_one_step, take_two_steps)

    # The final element in minimum_cost refers to the top floor
    return minimum_cost[-1]

# 449 µs ± 3.93 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
def minCostClimbingStairs2(cost: list[int]) -> int:
    def minimum_cost(i):
        # Base case, we are allowed to start at either step 0 or step 1
        if i <= 1:
            return 0

        # Check if we have already calculated minimum_cost(i)
        if i in memo:
            return memo[i]

        # If not, cache the result in our hash map and return it
        down_one = cost[i - 1] + minimum_cost(i - 1)
        down_two = cost[i - 2] + minimum_cost(i - 2)
        memo[i] = min(down_one, down_two)
        return memo[i]

    memo = {}
    return minimum_cost(len(cost))

# 404 µs ± 1.57 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
def minCostClimbingStairs21(cost: list[int]) -> int:
    @cache
    def minimum_cost(i):
        if i <= 1:
            return 0
        
        down_one = cost[i - 1] + minimum_cost(i - 1)
        down_two = cost[i - 2] + minimum_cost(i - 2)
        return min(down_one, down_two)

    return minimum_cost(len(cost))

# 188 µs ± 506 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
def minCostClimbingStairs3(cost: list[int]) -> int:        
    down_one = down_two = 0
    for i in range(2, len(cost) + 1):
        temp = down_one
        down_one = min(down_one + cost[i - 1], down_two + cost[i - 2])
        down_two = temp

    return down_one


def generateRandomCosts():
    return [random.randint(0,999) for _ in range(1000)]


