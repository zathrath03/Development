"""
You are a professional robber planning to rob houses along a street. Each
house has a certain amount of money stashed, the only constraint stopping you
from robbing each of them is that adjacent houses have security systems
connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the
police.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""


import unittest


class Solution:
    def rob(self, nums: list[int]) -> int:
        return 0


class Test(unittest.TestCase):
    test_cases = (
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
    )

    def test_rob(self):
        sol = Solution()
        for nums, expected in self.test_cases:
            assert sol.rob(nums) == expected
            print(f"test case {nums} passed")


if __name__ == "__main__":
    unittest.main()
