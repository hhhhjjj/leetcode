# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def removeLeafNodes(self, root, target):
        if root == target:
            if root.left:
                root = root.left
                self.removeLeafNodes(root, target)
            elif root.left is None and root.right is not None:
                root = root.right
                self.removeLeafNodes(root, target)
            else:
                root = None
        else:
            if root.left:
                self.removeLeafNodes(root.left, target)
            if root.right:
                self.removeLeafNodes(root.right, target)
        return root


root = TreeNode(1)
l1 = TreeNode(2)
r1 = TreeNode(3)
root.left = l1
root.right = r1
l2 = TreeNode(2)
r2 = TreeNode(2)
r3 = TreeNode(4)
l1.left = l2
r1.left =r2
r1.right = r3
print(Solution().removeLeafNodes(root, 2).left.val)


