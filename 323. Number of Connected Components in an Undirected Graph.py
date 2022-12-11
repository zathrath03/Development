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
        components: list[set[int]] = [set(edge) for edge in edges]

        self.consolidate_components(components)
        num_free_nodes = self.find_number_of_free_nodes(n, components)

        return len(components) + num_free_nodes

    def find_number_of_free_nodes(self, n, components):
        number_of_nodes_in_components = sum(
            [len(component) for component in components])
        free_nodes = n - number_of_nodes_in_components
        return free_nodes

    def consolidate_components(self, components):
        to_delete = []
        for i, component in enumerate(components):
            for other_component in components[i+1:]:
                if component.isdisjoint(other_component):
                    continue
                other_component |= component
                to_delete.append(i)
                break

        for i in reversed(to_delete):
            del components[i]


class Test(unittest.TestCase):
    test_cases = (
        (5, [[0, 1], [1, 2], [3, 4]], 2),
        (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1),
        (4, [[2, 3], [1, 2], [1, 3]], 2),
        (4, [[0, 1], [2, 3], [1, 2]], 1),
        (10, [[5, 6], [0, 2], [1, 7], [5, 9], [1, 8],
         [3, 4], [0, 6], [0, 7], [0, 3], [8, 9]], 1),
    )

    def test_countComponents(self):
        sol = Solution()
        for n, edges, expected in self.test_cases:
            assert sol.countComponents(n, edges) == expected
            print(f"passed test n={n}, edges={edges}")


if __name__ == "__main__":
    unittest.main()
