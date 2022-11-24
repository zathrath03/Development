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
        self.board = board
        self.word = word
        for row in range(len(board)):
            for col in range(len(board[0])):
                cell = row, col
                self.used = set()
                if self.is_word_here(cell, word):
                    return True

        return False

    def is_word_here(self, cell: tuple[int, int], word: str) -> bool:
        output = False
        row, col = cell

        if self.board[row][col] == word[0]:
            self.used.add(cell)
            if len(word) == 1:
                return True
            queue = self.valid_adjacent_cells(cell)
            if not queue:
                return False
            for next_cell in queue:
                output = self.is_word_here(next_cell, word[1:]) or output
            if not output:
                self.used.remove(cell)

        return output

    def valid_adjacent_cells(self, cell: tuple[int, int]
                             ) -> list[tuple[int, int]]:
        output = []
        row, col = cell
        adjacents = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for r_adj, c_adj in adjacents:
            new_cell = (row + r_adj, col + c_adj)
            if self.is_valid_cell(new_cell):
                output.append(new_cell)
        return output

    def is_valid_cell(self, cell):
        row, col = cell
        rows, cols = len(self.board), len(self.board[0])
        return cell not in self.used and 0 <= row < rows and 0 <= col < cols


class Test(unittest.TestCase):
    test_cases = (
        ([["B", "B", "C", "E"], ["S", "F", "C", "S"],
         ["A", "D", "E", "A"]], "A", True),
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
