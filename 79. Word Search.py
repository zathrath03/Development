"""
Given an m x n grid of characters board and a string word, return true if word
exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter
cell may not be used more than once.

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""


import unittest


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        return False


class Test(unittest.TestCase):
    test_cases = (
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]], "ABCCED", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]], "SEE", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]], "ABCB", False),
    )

    def test_exist(self):
        sol = Solution()
        for board, word, expected in self.test_cases:
            assert sol.exist(board, word) is expected


if __name__ == "__main__":
    unittest.main()
