# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> [int]:
        # 递归是挺简单的，在这试试迭代
        # 直接改值的话，就只能沿着最左边的线一直走下去，我想的是用个栈之类的记录一下
        if root is None:
            return None
        res = []
        if root:
            res.append(root.val)
            while root.left or root.right:
                while root.left:
                    root = root.left
                    res.append(root.val)
                while root.right:
                    root = root.right
                    res.append(root.val)
        return res


root = TreeNode(1)
R2 = TreeNode(2)
L3 = TreeNode(3)
L4 = TreeNode(4)
root.left = R2
R2.right = L4
root.right  =L3
print(Solution().inorderTraversal(root))
# 感觉我应该写个函数来自己构建链表，二叉树这些结构，不要每次都去手动构造