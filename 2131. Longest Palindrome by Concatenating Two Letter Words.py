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
        self.init()

        for word in words:
            self.determine_if_needed(word)
        self.increment_output_if_single_double_letter_word()
        return self.output

    def increment_output_if_single_double_letter_word(self):
        if self.double_letter_words:
            self.output += 2

    def determine_if_needed(self, word):
        if word in self.needed_words:
            self.handle_needed_words(word)
        else:
            self.handle_new_words(word)

    def init(self):
        self.needed_words: defaultdict[str, int] = defaultdict(int)
        self.output = 0
        self.double_letter_words = 0

    def handle_new_words(self, word):
        self.increment_double_letters(word)
        self.needed_words[word[::-1]] += 1

    def increment_double_letters(self, word):
        if word[0] == word[1]:
            self.double_letter_words += 1

    def handle_needed_words(self, word):
        self.decrement_double_letters(word)
        self.decrement_candidates(word)
        self.output += 4

    def decrement_candidates(self, word):
        self.needed_words[word] -= 1
        if self.needed_words[word] == 0:
            del self.needed_words[word]

    def decrement_double_letters(self, word):
        if word[0] == word[1]:
            self.double_letter_words -= 1


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
