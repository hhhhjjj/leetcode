# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        # 这个就前序遍历呗
        if root is None:
            return []
        res = []
        def helper(root,depth):
            if root:
                try:
                    res[depth].append(root.val)
                except:
                    res.append([root.val])
                depth += 1
                helper(root.left, depth)
                helper(root.right, depth)
        helper(root, 0)
        return res

T1 = TreeNode(3)
T2 = TreeNode(1)
T3 = TreeNode(5)
T4 = TreeNode(0)
T5 = TreeNode(2)
T6 = TreeNode(4)
T7 = TreeNode(6)
T1.left = T2
T1.right = T3
# T2.left = T4
# T2.right = T5
T3.left = T6
T3.right = T7
print(Solution().levelOrder(T1))