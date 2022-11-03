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


from collections import defaultdict
import unittest


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        candidates: defaultdict[str, int] = defaultdict(int)
        output = 0
        double_letter_words = 0

        for word in words:
            if word in candidates:
                if word[0] == word[1]:
                    double_letter_words -= 1
                candidates[word] -= 1
                if candidates[word] == 0:
                    del candidates[word]
                output += 4
            else:
                if word[0] == word[1]:
                    double_letter_words += 1
                candidates[word[::-1]] += 1
        if double_letter_words:
            output += 2
        return output


class Test(unittest.TestCase):
    test_cases = [
        (["lc", "cl", "gg"], 6),
        (["ab", "ty", "yt", "lc", "cl", "ab"], 8),
        (["cc", "ll", "xx"], 2),
        (["lc", "cl", "gg", "gg"], 8),
        (["qo", "fo", "fq", "qf", "fo", "ff", "qq", "qf",
         "of", "of", "oo", "of", "of", "qf", "qf", "of"], 14)
    ]

    def test_longestPalindrome(self):
        sol = Solution()
        for words, expected in self.test_cases:
            # assert sol.longestPalindrome(words) == expected
            print(sol.longestPalindrome(words), expected)


if __name__ == "__main__":
    unittest.main()
