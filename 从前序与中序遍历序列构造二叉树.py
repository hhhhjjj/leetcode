# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        if inorder == []:
            return None
        root = preorder[0]
        root_index = inorder.index(root)
        root = TreeNode(root)
        left_tree_mid = inorder[:root_index]
        right_tree_mid = inorder[root_index + 1:]
        # 中间部分怎么处理我知道，但是这个前序这里我卡住了
        # 其实还是我对前序的理解错了，这个前序不是层次遍历，如果有子树的话，肯定是在left与right中间的
        root.left = self.buildTree(preorder[1: root_index + 1], left_tree_mid)
        root.right = self.buildTree(preorder[root_index + 1:], right_tree_mid)
        return root

print(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]))





