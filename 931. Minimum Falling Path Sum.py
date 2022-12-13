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
        MAX_LENGTH = MAX_ELEMENT = 100
        n = len(matrix)
        window_ptrs = [[-i, i+1] for i in range(n)]
        min_per_window = [
            min(matrix[row][window_ptrs[row][0]:window_ptrs[row][1]]) for row in range(n)
        ]
        min_path_sum = MAX_LENGTH * MAX_ELEMENT + 1

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

        for i in range(n):
            min_path_sum = min(min_path_sum, sum(min_per_window))
            lft_ptr = max(window_ptrs[i][0], 0)
            rgt_ptr = min(window_ptrs[i][1], n - 1)
            # update the window's min with the next ele from the right
            min_per_window[i] = min(min_per_window[i], matrix[i][rgt_ptr])
            # slide the right edge of the window
            window_ptrs[i][1] += 1
            # get the new min if the old min is about to leave the window
            if window_ptrs[i][0] == min_per_window[i]:
                # TODO there has to be a better way to do this without min()
                min_per_window[i] = min(matrix[i][lft_ptr:rgt_ptr])
            # slide the left edge of the window
            window_ptrs[i][0] += 1

        min_path_sum = min(min_path_sum, sum(min_per_window))
        return min_path_sum


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
