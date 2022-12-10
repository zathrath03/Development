"""
Given the root of a binary tree, split the binary tree into two subtrees by
removing one edge such that the product of the sums of the subtrees is
maximized.

Return the maximum product of the sums of the two subtrees. Since the answer
may be too large, return it modulo 10^9 + 7.

Note that you need to maximize the answer before taking the mod and not after
taking it.

Constraints:
The number of nodes in the tree is in the range [2, 5 * 10^4].
1 <= Node.val <= 10^4
"""


import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: TreeNode | None) -> int:
        return 0


class Test(unittest.TestCase):
    test_cases = (
        ([1, 2, 3, 4, 5, 6], 110),
        ([1, None, 2, 3, 4, None, None, 5, 6], 90),
    )

    def test_maxProduct(self):
        sol = Solution()
        for root, expected in self.test_cases:
            root = self.deserialize(root)
            assert sol.maxProduct(root) == expected

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
