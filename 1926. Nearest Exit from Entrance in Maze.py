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


import unittest


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        # Use a breadth first search
        # Keep track of visited cells (set) - add entrance
        # Add the (entrance, 0) to a deque
        # While there are items in the queue, pop each cell
        # if the cell is not in visited and is adjacent to the end, return steps
        # Find valid adjacent cells and add them to the queue with steps
        # A valid square is within the bounds, has not been visited, and is "."
        # Add cell to visited and repeat
        # If we get to an empty queue, return -1
        return 0


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
