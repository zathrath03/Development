"""
Given an integer array nums and an integer k, return true if nums has a
continuous subarray of size at least two whose elements sum up to a multiple
of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that
x = n * k. 0 is always a multiple of k.

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= sum(nums[i]) <= 2^31 - 1
1 <= k <= 2^31 - 1
"""
import unittest


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        if sum(nums) % k == 0:
            return True

        return (self.checkSubarraySum(nums[:-1], k)
                or self.checkSubarraySum(nums[1:], k))


class Test(unittest.TestCase):
    test_cases = [
        ([23, 2, 4, 6, 7], 6, True),
        ([23, 2, 6, 4, 7], 6, True),
        ([23, 2, 6, 4, 7], 13, False)
    ]

    def test_checkSubarraySum(self):
        sol = Solution()
        for nums, k, expected in self.test_cases:
            assert sol.checkSubarraySum(nums, k) == expected


if __name__ == "__main__":
    unittest.main()
