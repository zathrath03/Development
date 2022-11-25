"""
Given an array of integers arr, find the sum of min(b), where b ranges over
every (contiguous) subarray of arr. Since the answer may be large, return the
answer modulo 10^9 + 7.

Constraints:
1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
"""


import unittest


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        return 0


class Test(unittest.TestCase):
    test_cases = (
        ([3, 1, 2, 4], 17),
        ([11, 81, 94, 43, 3], 444),
    )

    def test_sumSubarrayMins(self):
        sol = Solution()
        for arr, expected in self.test_cases:
            assert sol.sumSubarrayMins(arr) == expected


if __name__ == "__main__":
    unittest.main()
