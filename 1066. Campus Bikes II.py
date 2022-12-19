"""
On a campus represented as a 2D grid, there are n workers and m bikes, with
n <= m. Each worker and bike is a 2D coordinate on this grid.

We assign one unique bike to each worker so that the sum of the Manhattan
distances between each worker and their assigned bike is minimized.

Return the minimum possible sum of Manhattan distances between each worker and
their assigned bike.

The Manhattan distance between two points p1 and p2 is
Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
"""


class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]
                    ) -> int:
        return 0
