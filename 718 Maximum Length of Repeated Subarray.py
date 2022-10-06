from itertools import combinations


class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        subarrays = set()
        maxLength = 0
        for subarray in self.generateSubArrays(nums1):
            subarrays.add(subarray)
        for subarray in self.generateSubArrays(nums2):
            if subarray in subarrays:
                maxLength = max(maxLength, len(subarray))

        return maxLength

    def generateSubArrays(self, array: list) -> tuple:
        indices = list(range(len(array) + 1))
        for i, j in combinations(indices, 2):
            yield tuple(array[i:j])
