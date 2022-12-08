"""
Consider all the leaves of a binary tree, from left to right order, the values
of those leaves form a leaf value sequence.

          3
    5           1
6       2     9   8
      7   4

For example, in the given tree above, the leaf value sequence is
(6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is
the same.

Return true if and only if the two given trees with head nodes root1 and root2
are leaf-similar.

Constraints:
The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
"""


from collections import deque
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None
                    ) -> bool:
        if root1 is None or root2 is None:
            return False
        q = [root1]
        leafs1: deque[int] = deque()
        while q:
            node = q.pop()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if not node.left and not node.right:
                leafs1.append(node.val)

        q = [root2]
        while q:
            node = q.pop()
            if (not node.left and not node.right
                    and node.val != leafs1.popleft()):
                return False
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return True


class Test(unittest.TestCase):
    test_cases = (
        ([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4], [
         3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8], True),
        ([1, 2, 3], [1, 3, 2], False)
    )

    def test_leafSimilar(self):
        sol = Solution()
        for root1, root2, expected in self.test_cases:
            root1 = self.deserialize(root1)
            root2 = self.deserialize(root2)
            assert sol.leafSimilar(root1, root2) == expected

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
