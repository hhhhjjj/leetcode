# -*- coding: utf-8 -*-
class Solution:
    def removeDuplicates(self, nums):
        length = len(nums)
        if length < 2:
            return length
        # 这个题目不能直接用set来去重，然后还要求O1的空间复杂度
        # 也就是说不能先复制
        # nums = list(set(nums))
        i = length - 1
        while i != 0:
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                nums.pop(i)
            i = i - 1
        return len(nums)
# 题解是用双指针，相同的话就跳过，最后给慢指针的位置就行


print(Solution().removeDuplicates([1,1,2]))