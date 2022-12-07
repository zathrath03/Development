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

    def test_rangeSumBST(self):
        sol = Solution()
        for serialized_root, low, high, expected in self.test_cases:
            root = self.deserialize(serialized_root)
            assert sol.rangeSumBST(root, low, high) == expected

    def deserialize(self, serialized_root):
        if not serialized_root:
            return None
        nodes = [None if val is None else TreeNode(int(val))
                 for val in serialized_root]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root


if __name__ == "__main__":
    unittest.main()
