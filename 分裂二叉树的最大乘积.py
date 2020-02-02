# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxProduct(self, root):
        # 想要乘积尽可能大，两边最好相等
        sum_left = 0
        sum_right = 0
        