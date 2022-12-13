"""
Given an n x n array of integers matrix, return the minimum sum of any falling
path through matrix.

A falling path starts at any element in the first row and chooses the element
in the next row that is either directly below or diagonally left/right.
Specifically, the next element from position (row, col) will be
(row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100
"""


import unittest


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        return 0


class Test(unittest.TestCase):
    test_cases = (
        ([[2, 1, 3], [6, 5, 4], [7, 8, 9]], 13),
        ([[-19, 57], [-40, -5]], -59),
    )

    def test_minFallingPathSum(self):
        sol = Solution()
        for matrix, expected in self.test_cases:
            assert sol.minFallingPathSum(matrix) == expected
            print(f"Test case {matrix} passed")


if __name__ == "__main__":
    unittest.main()
