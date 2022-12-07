"""
Given the root node of a binary search tree and two integers low and high,
return the sum of values of all nodes with a value in the inclusive range
[low, high].

Constraints:
The number of nodes in the tree is in the range [1, 2 * 10^4].
1 <= Node.val <= 10^5
1 <= low <= high <= 10^5
All Node.val are unique.
"""

from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int
                    ) -> int:
        return 0


class Test(unittest.TestCase):
    test_cases = (
        ([10, 5, 15, 3, 7, None, 18], 7, 15, 32),
        ([10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10, 23),
    )
