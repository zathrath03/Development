"""
You are given an m x n integer matrix grid where each cell is either 0 (empty)
or 1 (obstacle). You can move up, down, left, or right from and to an empty
cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0)
to the lower right corner (m - 1, n - 1) given that you can eliminate at most
k obstacles. If it is not possible to find such walk return -1.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
"""


from typing import Union
import unittest


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        if k > num_rows + num_cols - 3:
            return num_rows + num_cols - 2
        visited: set[tuple[int, int]] = set()

        def recursive_path_search(row: int, col: int, remaining: int
                                  ) -> Union[int, float]:
            if (row < 0 or col < 0 or row > num_rows - 1 or col > num_cols - 1
                or (is_blocked := grid[row][col]) and remaining == 0
                    or (row, col) in visited):
                return float('inf')
            if row == num_rows - 1 and col == num_cols - 1:
                return 0
            visited.add((row, col))
            if is_blocked:
                remaining -= 1
            up = recursive_path_search(row - 1, col, remaining)
            down = recursive_path_search(row + 1, col, remaining)
            left = recursive_path_search(row, col - 1, remaining)
            right = recursive_path_search(row, col + 1, remaining)
            return 1 + min(up, down, left, right)

        if (length := recursive_path_search(0, 0, k)) < float('inf'):
            return int(length)
        return -1


class Test(unittest.TestCase):
    test_cases = [
        ([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1, 6),
        ([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1, -1),
        ([[0, 1, 0, 1],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [1, 0, 0, 1],
          [0, 1, 0, 0]],
         18, 7),
        ([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0]], 2, 5)
    ]

    def test_shortestPath(self):
        sol = Solution()
        for grid, k, expected in self.test_cases:
            assert sol.shortestPath(grid, k) == expected


if __name__ == "__main__":
    unittest.main()
