"""
Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing the relative order
of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both
strings.

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""


from collections import defaultdict
import unittest


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text1, text2 = text2, text1

        char_index_map = defaultdict(list)
        for index, char in enumerate(text1):
            char_index_map[char].append(index)

        subsequence_length = max_subsequence_length = 0
        last_index = -1
        for i, char in enumerate(text2):
            if char not in char_index_map:
                continue
            if index := next((index for index in char_index_map[char]
                              if index > last_index), False):
                subsequence_length += 1
                last_index = index
            else:
                pass


class Test(unittest.TestCase):
    test_cases = (
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("abcde", "cebcdea", 4),
        ("ace", "abcde", 3)
    )

    def test_longestCommonSubsequence(self):
        sol = Solution()
        for text1, text2, expected in self.test_cases:
            assert sol.longestCommonSubsequence(text1, text2) == expected
            print(f"case {text1}, {text2} passed")
