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
    # type: ignore
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        self.maze = maze
        start: tuple[int, int] = tuple(entrance)
        self.visited = {start}
        queue: deque[tuple[tuple[int, int], int]] = deque()
        queue.append((start, 0))
        while queue:
            cell, steps = queue.pop()
            row, col = cell
            if (self.is_exit(cell)):
                return steps
            for r_adj, c_adj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_cell = (row + r_adj, col + c_adj)
                if self.is_valid_cell(next_cell):
                    queue.appendleft((next_cell, steps + 1))
            self.visited.add(cell)
        return -1

    def is_exit(self, cell):
        row, col = cell
        last_row, last_col = len(self.maze) - 1, len(self.maze[0]) - 1
        return (cell not in self.visited
                and (not all(cell) or row == last_row or col == last_col))

    def is_valid_cell(self, cell: tuple[int, int]):
        row, col = cell
        return (0 <= row < len(self.maze) and 0 <= col < len(self.maze[0])
                and cell not in self.visited and self.maze[row][col] == ".")


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
