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

Constraints:
n == img1.length == img1[i].length
n == img2.length == img2[i].length
1 <= n <= 30
img1[i][j] is either 0 or 1.
img2[i][j] is either 0 or 1.
"""


import unittest


class Solution:
    def largestOverlap(self, img1: list[list[int]],
                       img2: list[list[int]]) -> int:
        # Find which img has the fewest number of 1s
        # -The fewest 1s will be our stationary image
        # -Provides the max we can possibly return if all 1s overlap
        # -Should give us a smaller target?

        # May be best to perform this recursively
        # Base case is the moving image has no ones
        if self.count_ones(img1) == 0:
            return 0
        # Check current overlap of both images
        overlap = self.count_overlap(img1, img2)
        left = self.largestOverlap(self.translate(img1, (-1, 0)), img2)
        right = self.largestOverlap(self.translate(img1, (1, 0)), img2)
        up = self.largestOverlap(self.translate(img1, (0, -1)), img2)
        down = self.largestOverlap(self.translate(img1, (0, 1)), img2)

        return max(overlap, left, right, up, down)
        # Set output to max(current value, new overlap)
        # Recursively call function translating left, right, up, down
        # Return max(self, left, right, up, down)

    def count_overlap(self, img1, img2):
        n = len(img1)
        count = 0
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1 and img2[i][j] == 1:
                    count += 1
        return count

    def count_ones(self, img: list[list[int]]) -> int:
        pass

    def translate(self, img: list[list[int]], dir: tuple[int, int]) -> list[list[int]]:
        pass


class Test(unittest.TestCase):
    test_cases = [
        ([[1, 1, 0], [0, 1, 0], [0, 1, 0]],
         [[0, 0, 0], [0, 1, 1], [0, 0, 1]], 3),
        ([[1]], [[1]], 1),
        ([[0]], [[0]], 0)
    ]

    def test_largestOverlap(self):
        sol = Solution()
        for img1, img2, expected in self.test_cases:
            assert sol.largestOverlap(img1, img2) == expected


if __name__ == "__main__":
    unittest.main()
