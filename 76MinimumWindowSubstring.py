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
from typing import Union
import unittest


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        t_counts = Counter(t)
        s_counts = Counter(s)
        if t_counts > s_counts:
            return ""

        possible_windows = self.find_possible_windows(s, t_counts)
        smallest_wdw = min(possible_windows,
                           key=lambda wdw: wdw[1] - wdw[0], default=None)
        return s[smallest_wdw[0]: smallest_wdw[1]+1] if smallest_wdw else ""

    def find_possible_windows(self, s, t_counts):
        possible_windows = []
        offset = 0
        while (window := self.find_window(s[offset:], t_counts)) is not None:
            lft = window[0] + offset
            rgt = window[1] + offset
            possible_windows.append((lft, rgt))
            offset = lft + 1
        return possible_windows

    def window_start(self, s: str, counts: Counter) -> Union[int, None]:
        for i, char in enumerate(s):
            if char in counts:
                return i
        return None

    def window_end(self, s: str, counts: Counter) -> Union[int, None]:
        present: Counter = Counter()

        for i, char in enumerate(s):
            if char in counts:
                present[char] = present.get(char, 0) + 1
                if present >= counts:
                    return i
        return None

    def find_window(self, s: str, counts: Counter) -> Union[tuple[int, int],
                                                            None]:
        lft = self.window_start(s, counts)
        if lft is None:
            return None
        if (right_inc := self.window_end(s[lft:], counts)) is None:
            return None
        rgt = lft + right_inc
        return (lft, rgt)


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
