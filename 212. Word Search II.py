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
from collections import defaultdict, deque
import unittest


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        first_letters = defaultdict(list)
        for i, word in enumerate(words):
            first_letters[word[0]].append(i)

        output = []
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter in first_letters:
                    cell = (i, j)
                    possible_words = [words[index]
                                      for index in first_letters[letter]]
                    output.extend(self.trace_word(cell, possible_words, board))
        return output

    def trace_word(self,
                   cell: tuple[int, int],
                   possible_words: list[str],
                   board: list[list[str]]
                   ) -> list[str]:
        # If any of the words have len of one, append it to output and remove it from possible words
        # Check the adjacent cells to see if any of them contain the ith letter of the possible words
        # - keep track of which index we're checking, starting at 1
        # - Add all adjacent cells to a queue
        # - While there are cells in the queue:
        # - - Check that the cell is within the bounds of the board
        # - - Check that the cell hasn't already been visited
        # - - Check if the letter in the cell equals the ith letter of any words
        # - - - If it does, add the cell to a list of cells to get adjacents to in the next pass
        # - - - If that is the last letter of the word, add it to the output and remove it from possible words
        # - Check the length of remaining words and remove any that we're at the end of
        output = []
        cells = [cell]
        queue = deque()
        while (len(possible_words) > 0):
            for cell in cells:
                for adjacent in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    queue.append((cell + adjacent))
        return output


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
