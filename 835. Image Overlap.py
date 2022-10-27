"""
You are given two images, img1 and img2, represented as binary, square
matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right,
up, and/or down any number of units. We then place it on top of the other
image. We can then calculate the overlap by counting the number of positions
that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits
that are translated outside of the matrix borders are erased.

Return the largest possible overlap.
"""


import unittest


class Solution:
    def largestOverlap(self, img1: list[list[int]],
                       img2: list[list[int]]) -> int:
        pass


class Test(unittest.TestCase):
    test_cases = [
        ([[1, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 1, 1], [0, 0, 1]], 3),
        ([[1]], [[1]], 1),
        ([[0]], [[0]], 0)
    ]

    def test_largestOverlap(self):
        sol = Solution()
        for img1, img2, expected in self.test_cases:
            assert sol.largestOverlap(img1, img2) == expected


if __name__ == "__main__":
    unittest.main()
