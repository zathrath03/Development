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
    def numSquares(self, n: int) -> int:

        def is_divided_by(n, count):
            if count == 1:
                return n in squares

            for square in squares:
                if (is_divided_by(n - square, count - 1)):
                    return True

        squares = {i ** 2 for i in range(int(sqrt(n)), 0, -1)}

        for count in range(1, 4):
            if is_divided_by(n, count):
                return count

        return 4  # Lagrange's four-square theorem shows that 4 is the max


class Test(unittest.TestCase):
    test_cases = (
        (9, 1),
        (12, 3),
        (13, 2),
        (31, 4),
    )

    def test_numSquares(self):
        sol = Solution()
        for n, expected in self.test_cases:
            assert sol.numSquares(n) == expected


if __name__ == "__main__":
    unittest.main()
