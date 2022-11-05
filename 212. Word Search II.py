"""
Given an m x n board of characters and a list of strings words, return all
words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same
letter cell may not be used more than once in a word.

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
import unittest


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        return []


class Test(unittest.TestCase):
    test_cases = [
        ([["o", "a", "a", "n"], ["e", "t", "a", "e"],
         ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
         ["oath", "pea", "eat", "rain"], ["eat", "oath"]),
        ([["a", "b"], ["c", "d"]], ["abcb"], [])
    ]

    def test_findWords(self):
        sol = Solution()
        for board, words, expected in self.test_cases:
            assert sol.findWords(board, words) == expected


if __name__ == "__main__":
    unittest.main()
