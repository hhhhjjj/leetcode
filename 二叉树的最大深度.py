# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 这个的话感觉用后序遍历加递归应该就行了
        return self.get_depth(root, 0)

    def get_depth(self, root_node, depth):
        if root_node is None:
            return depth
        else:
            depth += 1
            return max(self.get_depth(root_node.left, depth), self.get_depth(root_node.right, depth))


R3 = TreeNode(3)
L9 = TreeNode(9)
R20 = TreeNode(20)
R15 = TreeNode(15)
R7 = TreeNode(7)
R3.left = L9
R3.right = R20
R20.left = R15
R20.right = R7
print(Solution().maxDepth(R3))


