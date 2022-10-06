def preorderRecurs(root):                
    def solve(root, ans):
        if root:
            ans.append(root.val)
            for child in root.children:
                solve(child, ans)
        return ans
    return solve(root, [])

def preorder(root): 
    if not root:
        return []

    preorder = []        
    stack = [root]

    while stack:
        root = stack.pop()
        preorder.append(root.val)
        stack.extend(root.children[::-1])           

    return preorder

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

testTree = Node(1, [Node(2, []), Node(3, [Node(6, []), Node(7, [Node(11, [Node(14, [])])])]), Node(4, [Node(8, [Node(12, [])])]), Node(5, [Node(9, [Node(13, [])]), Node(10, [])])])