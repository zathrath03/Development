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


from collections import Counter, defaultdict
import unittest


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for chars in strs:
            sorted_chars = "".join(sorted(chars))
            anagrams[sorted_chars].append(chars)

        return list(anagrams.values())

    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for chars in strs:
            anagrams[tuple(sorted(chars))].append(chars)

        return list(anagrams.values())


test_case = ["eat", "tea", "tan", "ate", "nat", "bat"]
# class Test(unittest.TestCase):
#     test_cases = [
#         (["eat", "tea", "tan", "ate", "nat", "bat"], [
#          ["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
#         ([""], [[""]]),
#         (["a"], [["a"]])
#     ]

#     def test_groupAnagrams(self):
#         sol = Solution()
#         for strs, expected in self.test_cases:
#             # TODO figure out how to accepted expected in any order
#             assert sol.groupAnagrams(strs) == expected


# if __name__ == "__main__":
#     unittest.main()
