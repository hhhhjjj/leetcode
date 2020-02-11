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
        # 这个题目先计算总和，然后再两边来算
        # 去掉一条边的乘积等于子树总和乘以（总和-子树总和）
        self.sum = 0
        # 记得加上self，不然传不进去
        self.cur_t = 0
        # 得到总和
        def get_sum(r):
            if r:
                self.sum += r.val
                if not r.left and not r.right:
                    self.cur_t = r.val
                else:
                    get_sum(r.left)
                    get_sum(r.right)

        get_sum(root)
        self.target = self.sum / 2
        self.cur_x = abs(self.target - self.cur_t)

        def find_tar(r):
            if r:
                s = r.val
                s += find_tar(r.left)
                s += find_tar(r.right)
                cur_x = abs(s - self.target)
                if cur_x < self.cur_x:
                    self.cur_t = s
                    self.cur_x = cur_x
                return s
            else:
                return 0

        find_tar(root)
        return ((self.sum - self.cur_t) * self.cur_t) % 1000000007


l1 = TreeNode(1)
l2 = TreeNode(2)
r3 = TreeNode(3)
l4 = TreeNode(4)
l5 = TreeNode(5)
r6 = TreeNode(6)
l1.left = l2
l1.right = r3
l2.left = l4
l2.right = l5
r3.left = r6
print(Solution().maxProduct(l1))