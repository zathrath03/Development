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
        if root is None:
            return 0

        def subtree_sum(root: TreeNode | None) -> int:
            if root is None:
                return 0
            root.val += subtree_sum(root.left) + subtree_sum(root.right)
            return root.val

        subtree_sum(root.left)
        subtree_sum(root.right)

        parent_val, product, node = self.initialize_loop(root)
        last_product = product

        while node and product >= last_product:
            last_product = product
            parent_val, product, node = self.product_of_parent_and_subtree(
                node, parent_val)

        return last_product % (10 ** 9 + 7)

    def product_of_parent_and_subtree(self, node: TreeNode, parent_val):
        left_val = node.left.val if node.left else 0
        right_val = node.right.val if node.right else 0
        node_val = node.val - left_val - right_val
        parent_val += node_val
        if left_val < right_val:
            parent_val += left_val
            product = parent_val * right_val
            node = node.right  # type: ignore
        else:
            parent_val += right_val
            product = parent_val * left_val
            node = node.left  # type: ignore
        return parent_val, product, node

    def initialize_loop(self, root: TreeNode):
        left_val = root.left.val if root.left else 0
        right_val = root.right.val if root.right else 0
        if left_val < right_val:
            parent_val = left_val + root.val
            product = parent_val * right_val
            node = root.right
        else:
            parent_val = right_val + root.val
            product = left_val * parent_val
            node = root.left
        return parent_val, product, node


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

    def deserialize(self, serialized_root: list[int]) -> TreeNode | None:
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
