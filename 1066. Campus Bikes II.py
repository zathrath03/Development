"""
On a campus represented as a 2D grid, there are n workers and m bikes, with
n <= m. Each worker and bike is a 2D coordinate on this grid.

We assign one unique bike to each worker so that the sum of the Manhattan
distances between each worker and their assigned bike is minimized.

Return the minimum possible sum of Manhattan distances between each worker and
their assigned bike.

The Manhattan distance between two points p1 and p2 is
Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Constraints:
n == workers.length
m == bikes.length
1 <= n <= m <= 10
workers[i].length == 2
bikes[i].length == 2
0 <= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000
All the workers and the bikes locations are unique.
"""


class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]
                    ) -> int:
        return 0
