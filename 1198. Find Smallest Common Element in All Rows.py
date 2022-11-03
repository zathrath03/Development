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
        """
        initiate a list of pointers with a length equal to the number of rows to 0
        while the max of those pointers is less than length of a row
        Keep track of the largest value that a pointer is pointing to
        Iterate through each row.
        If the pointed to value is smaller than the current largest,
         move the pointer to the next value until its equal or larger
         if larger, set the largest to that value and move to the next row
        """
        return 0


class Test(unittest.TestCase):
    test_cases = [
        ([[1, 2, 3, 4, 5], [2, 4, 5, 8, 10],
          [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]], 5),
        [[1, 2, 3], [2, 3, 4], [2, 3, 5], 2]
    ]

    def test_smallestCommonElement(self):
        sol = Solution()
        for mat, expected in self.test_cases:
            assert sol.smallestCommonElement(mat) == expected


if __name__ == "__main__":
    unittest.main()
