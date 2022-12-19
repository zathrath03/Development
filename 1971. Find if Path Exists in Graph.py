"""
There is a bi-directional graph with n vertices, where each vertex is labeled
from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D
integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional
edge between vertex ui and vertex vi. Every vertex pair is connected by at
most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source
to vertex destination.

Given edges and the integers n, source, and destination, return true if there
is a valid path from source to destination, or false otherwise.

Constraints:
1 <= n <= 2 * 10^5
0 <= edges.length <= 2 * 10^5
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= source, destination <= n - 1
There are no duplicate edges.
There are no self edges.
"""


import unittest


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int,
                  destination: int) -> bool:
        return False


class Test(unittest.TestCase):
    test_cases = (
        (3, [[0, 1], [1, 2], [2, 0]], 0, 2, True),
        (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 0, False)
    )

    def test_validPath(self):
        sol = Solution()
        for n, edges, source, destination, expected in self.test_cases:
            assert sol.validPath(n, edges, source, destination) == expected


if __name__ == "__main__":
    unittest.main()
