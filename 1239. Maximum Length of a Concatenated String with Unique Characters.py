"""
You are given an array of strings arr. A string s is formed by the
concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting
some or no elements without changing the order of the remaining elements.

Constraints:
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
"""


import unittest


class Solution:
    def maxLength(self, arr: list[str]) -> int:
        substrings = [""]
        longest = 0

        for substring in arr:
            for i in range(len(substrings)):
                new_substring = substring + substrings[i]
                if len(new_substring) == len(set(new_substring)):
                    substrings.append(new_substring)
                    longest = max(longest, len(new_substring))
        return longest


class Test(unittest.TestCase):
    test_cases = [
        (["un", "iq", "ue"], 4),
        (["cha", "r", "act", "ers"], 6),
        (["abcdefghijklmnopqrstuvwxyz"], 26),
        (["ab", "cd", "cde", "cdef", "efg", "fgh", "abxyz"], 11)
    ]

    def test_maxLength(self):
        sol = Solution()
        for test, expected in self.test_cases:
            assert sol.maxLength(test) == expected


if __name__ == "__main__":
    unittest.main()
