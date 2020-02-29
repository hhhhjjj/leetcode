# -*- coding: utf-8 -*-
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        # 这个用哈希表没啥，直接排序取中间数也行
        if nums != []:
            nums.sort()
            return nums[len(nums//2)]
        else: return None