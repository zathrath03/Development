"""
You have a 2-D grid of size m x n representing a box, and you have n balls.
The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell
that can redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the
bottom-right corner and is represented in the grid as 1.
A board that redirects the ball to the left spans the top-right corner to the
bottom-left corner and is represented in the grid as -1.
We drop one ball at the top of each column of the box. Each ball can get stuck
in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped
pattern between two boards or if a board redirects the ball into either wall
of the box.

Return an array answer of size n where answer[i] is the column that the ball
falls out of at the bottom after dropping the ball from the ith column at the
top, or -1 if the ball gets stuck in the box.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is 1 or -1.
"""


import unittest


class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        # perform a dfs for each column in the grid
        # Check if stuck in current cell
        # - if current cell is 1, check if next cell is -1 or boundary
        # - if current cell is -1, check if prev cell is -1 or boundary
        # - can just add value of current cell to current column instead of
        #   using two cases
        # Keep track of cells that will trap balls so we don't need to check
        return [0]


class Test(unittest.TestCase):
    test_cases = [
        ([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1],
         [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]], [1, -1, -1, -1, -1]),
        ([[-1]], [-1]),
        ([[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1],
         [-1, -1, -1, -1, -1, -1]], [0, 1, 2, 3, 4, -1])
    ]

    def test_findBall(self):
        sol = Solution()
        for grid, expected in self.test_cases:
            assert sol.findBall(grid) == expected


if __name__ == "__main__":
    unittest.main()
