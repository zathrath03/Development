"""
Given an array of strings strs, group the anagrams together. You can return
the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly
once.

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


import unittest


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        pass


class Test(unittest.TestCase):
    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [
         ["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]])
    ]

    def test_groupAnagrams(self):
        sol = Solution()
        for strs, expected in self.test_cases:
            # TODO figure out how to accepted expected in any order
            assert sol.groupAnagrams(strs) == expected


if __name__ == "__main__":
    unittest.main()
