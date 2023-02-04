from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l2 = len(s2)
        l1 = len(s1)

        if l1 > l2:
            return False

        s1_char_counts = Counter(s1)
        s2_char_counts_in_window = Counter(s2[:l1])

        for i in range(l1, l2):
            if s1_char_counts == s2_char_counts_in_window:
                return True
            char_to_remove = s2[i - l1]
            char_to_add = s2[i]
            s2_char_counts_in_window[char_to_remove] -= 1
            s2_char_counts_in_window[char_to_add] += 1

        if s1_char_counts == s2_char_counts_in_window:
            return True

        return False
