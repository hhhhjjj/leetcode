# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(root_l, root_r):
            if root_l:
                if root_r is None:
                    return False
                else:
                    if root_l.left is None and root_l.right is None and root_r.left is None and root_r.right is None:
                        return True
            else:
                if root_r:
                    return False
                else:
                    return True
            if root_l.left:
                if root_r.right is None or root_l.left.val != root_r.right.val:
                    return False
            else:
                if root_r.right:
                    return False
            if root_l.right:
                if root_r.left is None or root_l.right.val != root_r.left.val:
                    return False
            else:
                if root_r.left:
                    return False

            return helper(root_l.left, root_r.right) and helper(root_l.right, root_r.left)
        return helper(root, root)
