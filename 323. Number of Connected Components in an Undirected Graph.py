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
        components: list[set[int]] = []
        added_to_component = False
        for node1, node2 in edges:
            for component in components:
                if node1 in component or node2 in component:
                    component.add(node1)
                    component.add(node2)
                    added_to_component = True
            if not added_to_component:
                new_component = {node1, node2}
                components.append(new_component)
            added_to_component = False

        for i, component in enumerate(components):
            for other_component in components[i+1:]:
                if component.isdisjoint(other_component):
                    continue
                other_component |= component
                del components[i]
                break

        number_of_nodes_in_components = sum(
            [len(component) for component in components])
        free_nodes = n - number_of_nodes_in_components
        return len(components) + free_nodes


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
            print(f"passed test n={n}, edges={edges}")


if __name__ == "__main__":
    unittest.main()
