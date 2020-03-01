# -*- coding: utf-8 -*-
class Solution:
    def trap(self, height: [int]) -> int:
        if height == []:
            return 0
        res = 0
        length = len(height)
        # 两个指针记录下两侧，选小的峰值，再算中间的
        # 右侧必须是上升的，一旦遇到下降的就暂停
        left_cur = 0
        right_cur = 0
        Flag = True
        # 当flag为真时候下降，False时候上升
        while right_cur < length - 1:
            if height[right_cur + 1] < height[right_cur] and Flag is False:
                min_num = min(height[right_cur], height[left_cur])
                # 大于最小值的都不去算
                for i in height[left_cur + 1:right_cur]:
                    if i < min_num:
                        res += min_num - i
                left_cur = right_cur
                Flag = True
            elif height[right_cur + 1] > height[right_cur] and Flag is True:
                if right_cur + 1 == length - 1:
                    # 当走到了最右侧还上升的时候也算一下
                    right_cur += 1
                    min_num = min(height[right_cur], height[left_cur])
                    for i in height[left_cur + 1:right_cur]:
                        if i < min_num:
                            res += min_num - i
                Flag = False
            right_cur +=1
        return res
#     感觉还是不行，要动态规划吧

print(Solution().trap([5,2,1,2,1,5]))
