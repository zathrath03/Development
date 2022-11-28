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
        # intialize an empty set of undefeated, losers, and one_loss
        undefeated, one_loss, losers = set(), set(), set()
        # iterate through each match
        for winner, loser in matches:
            # if the winner isn't in losers or one_loss, add to undefeated
            if winner not in losers and winner not in one_loss:
                undefeated.add(winner)
            if loser in losers:
                continue
        # if the loser is in undefeated, remove from undefeated
            if loser in undefeated:
                undefeated.remove(loser)
        # if the loser is in one_loss, remove from one_loss and add to losers
            if loser in one_loss:
                one_loss.remove(loser)
                losers.add(loser)
        # if the loser isn't in one_loss or losers, add to one_loss
            else:
                one_loss.add(loser)
        # convert undefeated and one_loss to sorted lists
        # combine undefeated and one_loss to elements of a list and return
        return [sorted(undefeated), sorted(one_loss)]


class Test(unittest.TestCase):
    test_cases = (
        ([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8],
         [4, 9], [10, 4], [10, 9]], [[1, 2, 10], [4, 5, 7, 8]]),
        ([[2, 3], [1, 3], [5, 4], [6, 4]], [[1, 2, 5, 6], []]),
    )

    def test_findWinners(self):
        sol = Solution()
        for matches, expected in self.test_cases:
            result = sol.findWinners(matches)
            print(result)
            assert sol.findWinners(matches) == expected


if __name__ == "__main__":
    unittest.main()
