"""
A row-sorted binary matrix means that all elements are 0 or 1 and each row of
the matrix is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of
the leftmost column with a 1 in it. If such an index does not exist, return -1.

You can't access the Binary Matrix directly. You may only access the matrix
using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index
(row, col) (0-indexed).
BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2
elements [rows, cols], which means the matrix is rows x cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged
Wrong Answer. Also, any solutions that attempt to circumvent the judge will
result in disqualification.

For custom testing purposes, the input will be the entire binary matrix mat.
You will not have access to the binary matrix directly.

Constraints:
rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in non-decreasing order.
"""

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    MAX_MATRIX_LENGTH = 100

    def leftMostColumnWithOne(self, binaryMatrix) -> int:

        self.binaryMatrix = binaryMatrix
        self.rows, self.cols = binaryMatrix.dimensions()
        self.leftmost_column_with_one = self.MAX_MATRIX_LENGTH + 1

        rows_with_ones = self.get_rows_with_ones()

        for row in rows_with_ones:
            self.binary_search_row(row)

        return (
            self.leftmost_column_with_one
            if self.leftmost_column_with_one <= self.MAX_MATRIX_LENGTH
            else -1
        )

    def binary_search_row(self, row: int) -> int:
        leftmost_column_with_one = self.MAX_MATRIX_LENGTH + 1
        left, right = 0, self.cols - 1

        while left <= right:
            mid = (left + right) // 2
            if self.binaryMatrix.get(row, mid) == 1:
                self.leftmost_column_with_one = min(
                    self.leftmost_column_with_one, mid
                )
                right = mid - 1
            else:
                left = mid + 1
                if left >= self.leftmost_column_with_one:
                    break

        return leftmost_column_with_one

    def get_rows_with_ones(self) -> set:
        rows_with_ones = set()
        for row in range(self.rows):
            if self.binaryMatrix.get(row, self.cols - 1) == 1:
                rows_with_ones.add(row)
        return rows_with_ones
