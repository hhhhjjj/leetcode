# -*- coding: utf-8 -*-
class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 这个题其实就是个排序题,但是要求常数空间的一趟扫描算法
        # 直接字典重新构建其实还是两趟扫描
        # 三种颜色我就构建个三指针来做,我想的是中间的不动，0和2全往两边调
        # 其实就是分三段，一个0的最右边界，一个当前，一个2的最左边界
        red_0 = 0
        now = 0
        blue_2 = len(nums) - 1
        while now <= blue_2:
            if nums[now] == 0:
                nums[red_0], nums[now] = nums[now], nums[red_0]
#                 直接在这位置调换就行了
                red_0 += 1
                now += 1
            elif nums[now] == 2:
                nums[blue_2], nums[now] = nums[now], nums[blue_2]
                blue_2 -= 1
            else:
                now += 1


print(Solution().sortColors([2,0,2,1,1,0]))
