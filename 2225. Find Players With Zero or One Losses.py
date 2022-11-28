"""
You are given an integer array matches where matches[i] = [winneri, loseri]
indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same
outcome.

Constraints:
1 <= matches.length <= 105
matches[i].length == 2
1 <= winneri, loseri <= 105
winneri != loseri
All matches[i] are unique.
"""


import unittest


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        return [[0]]


class Test(unittest.TestCase):
    test_cases = (
        ([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8],
         [4, 9], [10, 4], [10, 9]], [[1, 2, 10], [4, 5, 7, 8]]),
        ([[2, 3], [1, 3], [5, 4], [6, 4]], [[1, 2, 5, 6], []]),
    )

    def test_findWinners(self):
        sol = Solution()
        for matches, expected in self.test_cases:
            assert sol.findWinners(matches) == expected


if __name__ == "__main__":
    unittest.main()
