"""
Given the root of a binary tree, find the maximum value v for which there
exist different nodes a and b where v = |a.val - b.val| and a is an ancestor
of b.

A node a is an ancestor of b if either: any child of a is equal to b or any
child of a is an ancestor of b.

Constraints:
The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105
"""


import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode | None, max_ancestor=None,
                        min_ancestor=None, max_diff=0) -> int:
        if not root:
            return 0
        if max_ancestor is not None and min_ancestor is not None:
            max_diff = max(abs(root.val - max_ancestor),
                           abs(root.val - min_ancestor), max_diff)
            if root.val > max_ancestor:
                max_ancestor = root.val
            elif root.val < min_ancestor:
                min_ancestor = root.val
        else:
            max_ancestor = root.val
            min_ancestor = root.val

        left_max_diff = self.maxAncestorDiff(
            root.left, max_ancestor, min_ancestor, max_diff)
        right_max_diff = self.maxAncestorDiff(
            root.right, max_ancestor, min_ancestor, max_diff)

        return max(max_diff, left_max_diff, right_max_diff)


class Test(unittest.TestCase):
    test_cases = (
        # ([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13], 7),
        ([1, None, 2, None, 0, 3], 3),
    )

    def test_maxAncestorDiff(self):
        sol = Solution()
        for root, expected in self.test_cases:
            root = self.deserialize(root)
            assert sol.maxAncestorDiff(root) == expected

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
