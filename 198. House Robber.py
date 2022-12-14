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
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        if n == 3:
            return max(nums[0] + nums[2], nums[1])
        profit = {
            "three_houses_back": nums[0],
            "two_houses_back": nums[1],
            "last_house": nums[2] + nums[0]
        }

        for i in range(3, n):
            this_house_total = (
                nums[i]
                + max(profit["two_houses_back"], profit["three_houses_back"])
            )
            profit["three_houses_back"] = profit["two_houses_back"]
            profit["two_houses_back"] = profit["last_house"]
            profit["last_house"] = this_house_total
        return max(profit["last_house"], profit["two_houses_back"])


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
