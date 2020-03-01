# -*- coding: utf-8 -*-
class Solution:
    def trap(self, height: [int]) -> int:
        if height == []:
            return 0
        res = 0
        length = len(height)
        # 两个指针记录下两侧，选小的峰值，再算中间的
        left_cur = 0
        right_cur = length - 1
        # 两边往中间夹，省的找左右峰值麻烦
        left_max = 0
        right_max = 0
#     看了下题解，也是用的双指针，但是还记录了左边和右边的最大值
#         然后不停的走找最高的
        while (left_cur < right_cur):
            if height[left_cur] < height[right_cur]:
                if height[left_cur] > left_max:
                    left_max = height[left_cur]
                else:
#                     只要这个比前面走到的最大值小，就可以积水了
                    res += left_max - height[left_cur]
                left_cur += 1
            else:
                if height[right_cur] > right_max:
                    right_max = height[right_cur]
                else:
                    #                     只要这个比前面走到的最大值小，就可以积水了
                    res += right_max - height[right_cur]
                right_cur -= 1
        return res

print(Solution().trap([5,2,1,2,1,5]))
