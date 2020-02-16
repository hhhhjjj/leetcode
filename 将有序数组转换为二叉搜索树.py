# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        # 这个还是广度优先，选择中点作为根节点应该就没问题了

        if nums == []:
            # 判别的是用等于
            return None

        def helper(nums_in):
            length = len(nums_in)
            root_in = TreeNode(nums_in[length // 2])
            # print(root_in.val)
            # print(length//2)
            if length == 2:
                root_in.left = helper(nums_in[:length//2])
            elif length > 2:
                root_in.left = helper(nums_in[:length // 2])
                root_in.right = helper(nums_in[length//2 + 1:])
            return root_in
        return helper(nums)
# 这个还是太慢了，可以用原来的数组。但是改成操作指针而不是重新定义数组
print(Solution().sortedArrayToBST([]))
