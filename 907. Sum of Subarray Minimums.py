"""
Given an array of integers arr, find the sum of min(b), where b ranges over
every (contiguous) subarray of arr. Since the answer may be large, return the
answer modulo 10^9 + 7.

Constraints:
1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
"""


from typing import Iterator
import unittest


class Solution:
    MOD = 10**9 + 7

    def sumSubarrayMins(self, arr: list[int]) -> int:
        output = 0
        mins = self.generate_mins(arr)
        for val in mins:
            output += val
            output %= self.MOD
        return output

    def generate_mins(self, arr: list[int]) -> Iterator[int]:
        length = len(arr)
        for i in range(length):
            last_min = 30000
            for j in range(length - i):
                last_min = min(arr[i + j], last_min)
                yield last_min


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
