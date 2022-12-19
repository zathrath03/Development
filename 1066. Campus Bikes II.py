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
from math import inf
import unittest


class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]
                    ) -> int:
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        MAX_DISTANCE = 2000 * len(workers)

        # Naive approach
        # For each worker, calculate and store the distance to each bike
        # Store each distance in a 2D list
        distances: list[list[int]] = []
        for worker in workers:
            worker_distances: list[int] = []
            for bike in bikes:
                worker_distances.append(manhattan(worker, bike))
            distances.append(worker_distances)

        # Find the minimum total sum by finding every permutaton of distances
        min_sum = MAX_DISTANCE
        for permutation in permutations(range(len(distances))):
            total = 0
            for row, col in zip(distances, permutation):
                total += row[col]
            min_sum = min(min_sum, total)
        return min_sum


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
