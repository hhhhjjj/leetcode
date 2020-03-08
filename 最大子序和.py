# -*- coding: utf-8 -*-
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        # 动态规划或者贪心算法或者分治法
        # 我那滑动窗口写的贼垃圾
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            # 不需要两个指针，在这就是保留前面的数据，其实是动态规划
            if nums[i - 1] > 0:
                # 这里的nums[i]其实是前面所有的相加
                nums[i] += nums[i - 1]
                # 贪心算法也差不多
            max_sum = max(nums[i], max_sum)
        return max_sum

print(Solution().maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4]))
