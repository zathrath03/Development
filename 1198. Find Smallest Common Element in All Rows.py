"""
Given an m x n matrix mat where every row is sorted in strictly increasing
order, return the smallest common element in all rows.

If there is no common element, return -1.

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 104
mat[i] is sorted in strictly increasing order.
"""


import unittest


class Solution:
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        num_rows = len(mat)
        num_cols = len(mat[0])
        ptr = [0] * num_rows
        largest_current_value = mat[0][0]
        current_element = [0] * num_rows

        while True:
            for row in range(num_rows):
                while (ptr[row] < num_cols
                       and mat[row][ptr[row]] < largest_current_value):
                    ptr[row] += 1
                if (col := ptr[row]) == num_cols:
                    return -1
                largest_current_value = current_element[row] = mat[row][col]
                if len(set(current_element)) == 1:
                    return largest_current_value


class Test(unittest.TestCase):
    test_cases = [
        ([[1, 2, 3, 4, 5], [2, 4, 5, 8, 10],
          [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]], 5),
        [[[1, 2, 3], [2, 3, 4], [2, 3, 5]], 2],
        ([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
          [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], 0)
    ]

    def test_smallestCommonElement(self):
        sol = Solution()
        for mat, expected in self.test_cases:
            # assert sol.smallestCommonElement(mat) == expected
            print(sol.smallestCommonElement(mat), expected)


if __name__ == "__main__":
    unittest.main()
