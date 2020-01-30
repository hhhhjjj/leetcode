# -*- coding: utf-8 -*-
class Solution:
    def containsDuplicate(self, nums):
        # 这个就是判断数组存在不存在重复元素
        # 感觉直接一个去重来判断长度就行了
        length = len(nums)
        if length < 2:
            return False
        length1 = len(list(set(nums)))
        if length1 == length:
            return False
        else:
            return True
# 这个题目还可以用排序来做
# 在数据量较小的时候，其实哈希表还没列表快
print(Solution().containsDuplicate([1,2,3,1]))