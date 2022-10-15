"""
Run-length encoding is a string compression method that works by replacing
consecutive identical characters (repeated 2 or more times) with the
concatenation of the character and the number marking the count of the
characters (length of the run). For example, to compress the string "aabccc"
we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string
becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters
from s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting
at most k characters.
"""

from functools import cache
import unittest


def getLengthOfOptimalCompression(s: str, k: int) -> int:
    @cache
    def dp(idx: int, last_char: str, last_char_count: int, k: int) -> int:
        if k < 0:
            return float('inf')
        if idx == n:
            return 0

        delete_char = dp(idx + 1, last_char, last_char_count, k - 1)
        if s[idx] == last_char:
            keep_char = dp(idx + 1, last_char, last_char_count +
                           1, k) + (last_char_count in {1, 9, 99})
        else:
            keep_char = dp(idx + 1, s[idx], 1, k) + 1

        return min(delete_char, keep_char)

    n = len(s)
    return dp(0, "", 0, k)


class Test(unittest.TestCase):
    test_cases = (
        ("aaabcccd", 2, 4),
        ("aabbaa", 2, 2),
        ("aaaaaaaaaaa", 0, 3)
    )

    def test_glooc(self):
        for s, k, expected in self.test_cases:
            assert getLengthOfOptimalCompression(s, k) == expected


if __name__ == "__main__":
    unittest.main()
