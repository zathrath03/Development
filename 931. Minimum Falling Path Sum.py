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


from math import inf
import unittest


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        min_path_sum = inf

        # Conceptually, I want to do a single pass with a stair-stepped
        # Pyramid. Each row will contain one or two more elements (depending
        # on whether or not we're against a boundry) from the previous row.
        # Treat it like a sliding window in each row where left and right
        # pointers are one column wider than the previous row
        # Keep track of the min in each row's window (and the second min?)
        # When we slide the window, if the element we gained from the right
        # is smaller than the min, update the min for that row's window.
        # If we slide the window off of the min, update the min to the second
        # min.
        # Once we have the mins for each row's windows, sum those mins.
        # If the sum is smaller than the min_path_sum, save as min_path_sum
        # Repeat until all first row elements are exhausted
        for first_element in matrix[0]:
            pass

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
