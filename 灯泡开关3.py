# -*- coding: utf-8 -*-
class Solution:
    def numTimesAllBlue(self, light: [int]) -> int:
        if light == []:
            return 0
        # 发现没那么复杂
        length = len(light)
        res = 0
        max_num = 0
        now_sum = 0
        for i in range(length):
            if light[i] > max_num:
                max_num = light[i]
                now_sum += 1
            else:
                now_sum += 1
            if max_num == now_sum:
                res += 1
        return res

print(Solution().numTimesAllBlue([4,1,2,3]))




