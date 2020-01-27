# -*- coding: utf-8 -*-
class Solution:
    def maxValueAfterReverse(self, nums):
        # 之前暴力方法超时了，其实有时候看数据量就知道n的二次方会超时
        # 其实这个绝对值公式可以想着怎么拆开
        # 改成用贪心算法,复杂度为n
        length = len(nums)
        if length < 2:
            return 0
        if length == 2:
            return abs(nums[0] - nums[1])
        # 一个数组的数组值可以表示成最大的nums[i] - nums[i + 1]-最小的nums[i] - nums[i + 1]
        # 找到了最大和最小，然后翻转就是第一项和第二项反过来
        # 所以第一项选择最小的，第二项选择最大的
        sum_init = sum([abs(nums[i] - nums[i - 1]) for i in range(1, length)])
        second_max = max(min(num[i], nums[i - 1]) for )




print(Solution().maxValueAfterReverse([2,3,1,5,4]))