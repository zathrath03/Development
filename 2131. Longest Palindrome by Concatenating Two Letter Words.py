"""
You are given an array of strings words. Each element of words consists of two
lowercase English letters.

Create the longest possible palindrome by selecting some elements from words
and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is
impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

Constraints:
1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.
"""


import unittest


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        """
        Iterate through the list
        If the word is a double letter, set a flag for DL encountered
        Check if the word is in a set
        If it is, add four to the output and remove the word from the set
        If it is not, add its reverse to the set
        Once through the list, add two to the output if the double letter flag is set
        Return the output
        """
        return 0


class Test(unittest.TestCase):
    test_cases = [
        (["lc", "cl", "gg"], 6),
        (["ab", "ty", "yt", "lc", "cl", "ab"], 8),
        (["cc", "ll", "xx"], 2)
    ]

    def test_longestPalindrome(self):
        sol = Solution()
        for words, expected in self.test_cases:
            assert sol.longestPalindrome(words) == expected


if __name__ == "__main__":
    unittest.main()
