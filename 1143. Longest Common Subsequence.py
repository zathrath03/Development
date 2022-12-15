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
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        len1 = len(text1)
        len2 = len(text2)

        previous = [0] * (len1 + 1)
        current = [0] * (len1 + 1)

        for col in range(len2 - 1, -1, -1):
            for row in range(len1 - 1, -1, -1):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            previous, current = current, previous

        return previous[0]


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
            print(f'case "{text1}", "{text2}" passed')


if __name__ == "__main__":
    unittest.main()
