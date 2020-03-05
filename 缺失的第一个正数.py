# -*- coding: utf-8 -*-
class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        if nums == []:
            return 1
        # 负数直接过掉，排序去重
        # 注意这个还可以重复的

        nums = list(set(nums))
        nums.sort()
        # 这里面肯定是可以继续优化的，我这其实都已经遍历了好几次了
        cur = 0
        num = 1
        length = len(nums)
        while cur < length:
            if nums[cur] > 0:
                if nums[cur] != num:
                    return num
                else:
                    num += 1
            cur += 1
        return num

# 看了下题解，把这些全部插入哈希表作为索引，然后从1开始查询

print(Solution().firstMissingPositive([1,1000]))











