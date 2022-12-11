"""
You have a graph of n nodes. You are given an integer n and an array edges
where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in
the graph.

Return the number of connected components in the graph.

Constraints:
1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
"""


import unittest


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        return 0


class Test(unittest.TestCase):
    test_cases = (
        (5, [[0, 1], [1, 2], [3, 4]], 2),
        (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1),
        (4, [[2, 3], [1, 2], [1, 3]], 2),
        (4, [[0, 1], [2, 3], [1, 2]], 1),
    )

    def test_countComponents(self):
        sol = Solution()
        for n, edges, expected in self.test_cases:
            assert sol.countComponents(n, edges) == expected


if __name__ == "__main__":
    unittest.main()
