"""
Given the coordinates of two rectilinear rectangles in a 2D plane, return the
total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its
top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its
top-right corner (bx2, by2).

Constraints:
-104 <= ax1 <= ax2 <= 104
-104 <= ay1 <= ay2 <= 104
-104 <= bx1 <= bx2 <= 104
-104 <= by1 <= by2 <= 104
"""


import unittest


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int,
                    by1: int, bx2: int, by2: int) -> int:
        # Find area of each rectangle
        # - (x2 - x1) * (y2 - y1) and sum them
        area = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        # Determine if there is overlap between the rectangles
        # - (bx1 < ax2 < bx2 or bx1 < ax1 < bx2)
        #     and (by1 <= ay1 < by2) or (by1 < ay2 <= by2)
        # - (by1 < ay2 < by2 or by1 < ay1 < by2)
        #     and (bx1 <= ax1 < bx2) or (bx1 < ax2 <= by2)
        # If there is overlap, subtract the area of the overlapping rectangle
        return area


class Test(unittest.TestCase):
    test_cases = [
        ((0, 0, 2, 2, -2, -2, 0, 0), 8),
        # ((-3, 0, 3, 4, 0, -1, 9, 2), 45),
        # ((-2, -2, 2, 2, -2, -2, 2, 2), 16)
    ]

    def test_computeArea(self):
        sol = Solution()
        for args, expected in self.test_cases:
            assert sol.computeArea(*args) == expected


if __name__ == "__main__":
    unittest.main()
