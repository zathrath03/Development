"""
Given two strings s and t of lengths m and n respectively, return the minimum
window substring of s such that every character in t (including duplicates) is
included in the window. If there is no such substring, return the empty string.

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
"""


from collections import Counter
import unittest


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Create a dict of char: count for the chars in t
        t_counts = Counter(t)

        # Find start of window
        # Find end of window where all items in t are in the window
        # Save window indexes as a possibility
        # Shift the window
        # # repeat the window search above on a substring
        # # use the index after the current start as the start of the substring
        # Return "" if no window indexes saved
        # Check the saved window indexes for the smallest length
        # Return the substring of the smallest length


class Test(unittest.TestCase):
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", "")
    ]

    def test_minWindow(self):
        sol = Solution()
        for s, t, expected in self.test_cases:
            assert sol.minWindow(s, t) == expected


if __name__ == "__main__":
    unittest.main()
