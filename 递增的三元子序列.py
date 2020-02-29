# -*- coding: utf-8 -*-
class Solution:
    def increasingTriplet(self, nums: [int]) -> bool:
        # 这个子序列不要求是连续的,在这我用两次遍历来完成
        length = len(nums)
        if length < 3:
            return False
        init_num = nums[0]
        add_num = 1
        for i in range(1,length):
            if init_num < nums[i]:
                add_num +=1
                init_num = nums[i]
            if add_num >= 3:
                return True
        init_num = nums[-1]
        add_num = 1
        for i in range(length - 2, -1, -1):
            if init_num > nums[i]:
                add_num += 1
                init_num = nums[i]
            if add_num >= 3:
                return True
        return False
# 其实这个直接双指针，保存两个较小数，然后在后面找到一个同时大于m1和m2的数就行
# 最小的数肯定序列是在最前面。即使发生了改变

