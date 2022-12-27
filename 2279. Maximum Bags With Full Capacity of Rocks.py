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
1 <= n <= 5 * 10^4
1 <= capacity[i] <= 10^9
0 <= rocks[i] <= capacity[i]
1 <= additionalRocks <= 10^9
"""


import unittest


class Solution:
    def maximumBags(
        self, capacity: list[int], rocks: list[int], additionalRocks: int
    ) -> int:
        # Determine the remaining capacity in each bag and store it in a list
        remaining_capacity = [c - r for c, r in zip(capacity, rocks)]
        # Sort the remaining capacity list smallest to largest
        remaining_capacity.sort()
        # While there are additional rocks remaining,
        i = full_bags = 0
        while additionalRocks > 0 and i < len(remaining_capacity):
            # iterate through the remaining capacity
            # Subtract each remaining capacity from additional rocks
            additionalRocks -= remaining_capacity[i]

            # Increment full bags if the remaining capacity reaches zero
            if additionalRocks >= 0:
                full_bags += 1
            i += 1
        # return full bags
        return full_bags


class Test(unittest.TestCase):
    test_cases = (
        ([2, 3, 4, 5], [1, 2, 4, 4], 2, 3),
        ([10, 2, 2], [2, 2, 0], 100, 3),
    )

    def test_maximumBags(self) -> None:
        sol = Solution()
        for capacity, rocks, additionalRocks, expected in self.test_cases:
            assert (
                sol.maximumBags(capacity, rocks, additionalRocks) == expected
            )


if __name__ == "__main__":
    unittest.main()
