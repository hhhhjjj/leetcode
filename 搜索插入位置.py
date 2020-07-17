# -*- coding: utf-8 -*-
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        # 这题目就别从头到尾了，查找的话一般就二分吧
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left