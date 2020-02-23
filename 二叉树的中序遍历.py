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
        # 左中右
        if root is None:
            return None
        res = []
        stack = []
        while stack or root:
            # 不断往左子树方向走，每走一次就将当前节点保存到栈中
            # 这是模拟递归的调用
            if root:
                stack.append(root)
                root = root.left
            # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
            # 然后转向右边节点，继续上面整个过程
            else:
                # 看来这是把所有的都放到栈里面去了
                # 然后给的时候不要给中，要给右，这样才不会变成死循环
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res



root = TreeNode(1)
R2 = TreeNode(2)
L3 = TreeNode(3)
L4 = TreeNode(4)
root.left = R2
R2.right = L4
root.right = L3
print(Solution().inorderTraversal(root))
# 感觉我应该写个函数来自己构建链表，二叉树这些结构，不要每次都去手动构造