# -*- coding: utf-8 -*-
class Solution:
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        if nums == []:
            return []
        length = len(nums)
        res = [0] * length
        if length == 1:
            return res
        for i in range(length):
            for j in range(i + 1, length):
                if nums[j] < nums[i]:
                    res[i] += 1
                elif nums[j] > nums[i]:
                    res[j] += 1
        return res


print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))