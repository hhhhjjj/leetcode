# -*- coding: utf-8 -*-
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        # 一年前做过，写的贼垃圾，现在来重新写下
        # 首先肯定不用n方的时间复杂度了
        if nums == []:
            return []
        num_dict = {}
        for index, num in enumerate(nums):
            # 这个先index后值
            if num_dict.get(target - num) is not None:
                # 要注意这里为0的时候if是会被判false的，所以要写清楚不是none
                return [num_dict[target - num], index]
            else:
                num_dict[num] = index

print(Solution().twoSum(nums = [2, 7, 11, 15], target = 9))