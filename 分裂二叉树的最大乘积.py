# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxProduct(self, root):
        # 想要乘积尽可能大，两边越接近越大

        def get_sum(root):
            res = root.val
            if root.left:
                res += get_sum(root.left)
            if root.right:
                res += get_sum(root.right)
            return res

        sum_left = root.val + get_sum(root.left)
        sum_right = get_sum(root.right)
        res = sum_left * sum_right
        res_left = (sum_left - root.val) * (sum_right + root.val)

        