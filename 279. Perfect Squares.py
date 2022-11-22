"""
Given an integer n, return the least number of perfect square numbers that sum
to n.

A perfect square is an integer that is the square of an integer; in other
words, it is the product of some integer with itself. For example, 1, 4, 9,
and 16 are perfect squares while 3 and 11 are not.

Constraints:
1 <= n <= 104
"""


from functools import cache
from math import sqrt
import unittest


class Solution:
    @cache
    def numSquares(self, n: int):
        squares = {i ** 2 for i in range(int(sqrt(n)), 0, -1)}
        if n in squares:
            return 0

        count = float('inf')

        for square in squares:
            count = min(count, 1 + self.numSquares(n - square))

        return count


class Test(unittest.TestCase):
    test_cases = (
        # (9, 1),
        (12, 3),
        (13, 2),
    )

    def test_numSquares(self):
        sol = Solution()
        for n, expected in self.test_cases:
            assert sol.numSquares(n) == expected


if __name__ == "__main__":
    unittest.main()
