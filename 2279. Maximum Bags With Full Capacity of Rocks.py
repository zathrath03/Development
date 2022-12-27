"""
You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer
arrays capacity and rocks. The ith bag can hold a maximum of capacity[i] rocks
and currently contains rocks[i] rocks. You are also given an integer
additionalRocks, the number of additional rocks you can place in any of the
bags.

Return the maximum number of bags that could have full capacity after placing
the additional rocks in some bags.

Constraints:
n == capacity.length == rocks.length
1 <= n <= 5 * 104
1 <= capacity[i] <= 109
0 <= rocks[i] <= capacity[i]
1 <= additionalRocks <= 109
"""


class Solution:
    def maximumBags(
        self, capacity: list[int], rocks: list[int], additionalRocks: int
    ) -> int:
        return 0