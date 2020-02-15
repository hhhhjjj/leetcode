# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            # 以后要设置一个值的话就用这种无穷大无穷小的来就行了
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                # 在这把上下界也给放进去判断
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

T1 = TreeNode(3)
T2 = TreeNode(1)
T3 = TreeNode(5)
T4 = TreeNode(0)
T5 = TreeNode(2)
T6 = TreeNode(4)
T7 = TreeNode(6)
T1.left = T2
T1.right = T3
T2.left = T4
T2.right = T5
T3.left = T6
T3.right = T7
print(Solution().isValidBST(T1))
