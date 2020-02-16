# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        # 这个还是广度优先，选择中点作为根节点应该就没问题了
        length =  len(nums)
        if length == 0:
            return TreeNode(None)
        if length == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[length // 2])
        def helper(root_in, nums_in):
            root_in = TreeNode(nums_in[length // 2])
        helper(root, nums)
        return root


