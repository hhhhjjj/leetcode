# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                # 这个就没啥技术了，这个是二次遍历
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
# 在这的话将dp变成排序列表，通过二分遍历这里面的元素
# 就是贪心算法，希望上升子序列最后加上的那个数尽可能小
