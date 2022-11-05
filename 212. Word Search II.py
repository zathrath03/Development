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
                    possible_words = set()
                    for index in first_letters[letter]:
                        if len(word := words[index]) == 1:
                            output.append(word)
                        else:
                            possible_words.add(word)
                    output.extend(self.trace_word(cell, possible_words, board))
        return list(set(output))

    def trace_word(self,
                   cell: tuple[int, int],
                   possible_words: set[str],
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
        visited = set()
        visited.add(cell)
        letter_index = 1
        while (len(possible_words) > 0):
            while cells:
                cell = cells.pop()
                for adjacent in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    if (adj_cell := tuple(map(sum, zip(cell, adjacent)))) not in visited:
                        queue.append(adj_cell)
            while queue:
                cell = queue.pop()
                if (cell[0] < 0 or cell[0] >= len(board)
                        or cell[1] < 0 or cell[1] >= len(board[0])):
                    continue
                for word in possible_words.copy():
                    if (len(word) == letter_index + 1
                            and word[-1] == board[cell[0]][cell[1]]):
                        output.append(word)
                        possible_words.remove(word)
                    elif word[letter_index] == board[cell[0]][cell[1]]:
                        cells.append(cell)
                visited.add(cell)
            letter_index += 1
            for word in possible_words.copy():
                if len(word) == letter_index:
                    possible_words.remove(word)

        return output


class Test(unittest.TestCase):
    test_cases = [
        ([["o", "a", "a", "n"], ["e", "t", "a", "e"],
         ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
         ["oath", "pea", "eat", "rain"], ["eat", "oath"]),
        ([["a", "b"], ["c", "d"]], ["abcb"], []),
        ([["a"]], ["a"], ["a"]),
        ([["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"],
         ["a", "f", "l", "v"]], ["oa", "oaa"], ["oa", "oaa"]),
        ([["a", "b", "c", "e"], ["x", "x", "c", "d"],
         ["x", "x", "b", "a"]], ["abc", "abcd"], ["abc", "abcd"])
    ]

    def test_findWords(self):
        sol = Solution()
        for board, words, expected in self.test_cases:
            print(sol.findWords(board, words))
            assert set(sol.findWords(board, words)) == set(expected)


if __name__ == "__main__":
    unittest.main()
