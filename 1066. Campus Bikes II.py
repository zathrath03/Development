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


from itertools import permutations
import unittest


# class Solution:
#     def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]
#                     ) -> int:
#         def manhattan(p1, p2):
#             return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
#         MAX_DISTANCE = 2000 * len(workers)

#         # Naive approach
#         # For each worker, calculate and store the distance to each bike
#         # Store each distance in a 2D list
#         distances: list[list[int]] = []
#         for worker in workers:
#             worker_distances: list[int] = []
#             for bike in bikes:
#                 worker_distances.append(manhattan(worker, bike))
#             distances.append(worker_distances)

#         # Find the minimum total sum by finding every permutaton of distances
#         min_sum = MAX_DISTANCE
#         for permutation in permutations(range(len(distances))):
#             total = 0
#             for row, col in zip(distances, permutation):
#                 total += row[col]
#             min_sum = min(min_sum, total)
#         return min_sum


class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]
                    ) -> int:
        MAX_DISTANCE = 2000 * len(workers)
        m, n = len(workers), len(bikes)
        # 0 ~ m - 1  workers
        # m ~ m + n - 1 bikes
        s = m + n  # dummy source
        t = s + 1  # dummy sink
        num_nodes = m + n + 2
        g: list[dict] = [{} for _ in range(num_nodes)]
        prevv: list[int] = [None] * num_nodes  # type: ignore

        def add_edge(from_node: int, to_node: int, cost: int
                     ) -> None:
            g[from_node][to_node] = [1, cost]
            # reverse edge
            g[to_node][from_node] = [0, -cost]

        def add_all_edges():
            for i in range(m):
                for j in range(n):
                    x1, y1 = workers[i]
                    x2, y2 = bikes[j]
                    c = abs(x1 - x2) + abs(y1 - y2)
                    add_edge(i, m + j, c)
            for i in range(m):
                add_edge(s, i, 0)
            for i in range(n):
                add_edge(m + i, t, 0)

        # find minimum cost to flow f from s to t
        def min_cost_flow(s: int, t: int, f: int) -> int:
            res = 0
            # Bellman-Ford
            while f > 0:
                dist = [MAX_DISTANCE] * (m + n + 2)
                dist[s] = 0
                update = True
                while update:
                    update = False
                    for v in range(num_nodes):
                        if dist[v] == MAX_DISTANCE:
                            continue
                        for node in g[v]:
                            edge = g[v][node]
                            # if there is capacity left on this edge and
                            # it costs less to go to the next node from here
                            if edge[0] > 0 and dist[node] > dist[v] + edge[1]:
                                dist[node] = dist[v] + edge[1]
                                prevv[node] = v
                                update = True
                assert dist[t] != MAX_DISTANCE
                d = f
                v = t
                while v != s:
                    d = min(d, g[prevv[v]][v][0])
                    v = prevv[v]
                f -= d
                res += d * dist[t]
                v = t

                while v != s:
                    # remove capacity from used edge
                    edge = g[prevv[v]][v]
                    edge[0] -= d
                    # add capacity to reverse edge
                    edge = g[v][prevv[v]]
                    edge[0] += d
                    v = prevv[v]
            return res

        add_all_edges()

        return min_cost_flow(s, t, m)


class Test(unittest.TestCase):
    test_cases = (
        ([[0, 0], [2, 1]], [[1, 2], [3, 3]], 6),
        ([[0, 0], [1, 1], [2, 0]], [[1, 0], [2, 2], [2, 1]], 4),
        ([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]], [
         [0, 999], [1, 999], [2, 999], [3, 999], [4, 999]], 4995),
        ([[239, 904], [191, 103], [260, 117], [86, 78], [747, 62]],
         [[660, 8], [431, 772], [78, 576], [894, 481], [451, 730], [155, 28]],
         1886),
    )

    def test_assignBikes(self):
        sol = Solution()
        for workers, bikes, expected in self.test_cases:
            assert sol.assignBikes(workers, bikes) == expected


if __name__ == "__main__":
    unittest.main()
