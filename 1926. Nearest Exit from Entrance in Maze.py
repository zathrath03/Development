"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented
as '.') and walls (represented as '+'). You are also given the entrance of the
maze, where entrance = [entrancerow, entrancecol] denotes the row and column
of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step
into a cell with a wall, and you cannot step outside the maze. Your goal is to
find the nearest exit from the entrance. An exit is defined as an empty cell
that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the
nearest exit, or -1 if no such path exists.

Constraints:
maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] is either '.' or '+'.
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance will always be an empty cell.
"""


from collections import deque
import unittest


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        self.maze = maze

        maze[entrance[0]][entrance[1]] = "+"
        queue: deque[tuple[list[int], int]] = deque()
        queue.append((entrance, 0))
        output = -1

        while queue:
            output = self.find_exit(queue)
        return output

    def find_exit(self, queue):
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        cell, steps = queue.pop()
        row, col = cell
        for r_adj, c_adj in directions:
            next_cell = [row + r_adj, col + c_adj]
            if self.is_valid_cell(next_cell):
                if self.is_exit(next_cell):
                    return steps + 1
                queue.appendleft((next_cell, steps + 1))
                self.maze[row][col] = "+"
        return -1

    def is_exit(self, cell):
        row, col = cell
        last_row, last_col = len(self.maze) - 1, len(self.maze[0]) - 1
        return (self.maze[row][col] == "."
                and (not all(cell) or row == last_row or col == last_col))

    def is_valid_cell(self, cell: list[int]):
        row, col = cell
        rows, cols = len(self.maze), len(self.maze[0])
        return (0 <= row < rows and 0 <= col < cols
                and self.maze[row][col] == ".")


class Test(unittest.TestCase):
    test_cases = (
        ([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]],
         [1, 2], 1),
        ([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0], 2),
        ([[".", "+"]], [0, 0], -1)
    )

    def test_nearestExit(self):
        sol = Solution()
        for maze, entrance, expected in self.test_cases:
            assert sol.nearestExit(maze, entrance) == expected


if __name__ == "__main__":
    unittest.main()
