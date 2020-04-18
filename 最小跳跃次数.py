# -*- coding: utf-8 -*-
class Solution:
    def minJump(self, jump: [int]) -> int:
        # 之前的题目是问能不能跳出去，现在这个就要求最小的跳跃次数
        n = len(jump)
        step_list = [1] * n
        max_num = 0
        for i in range(n):
            if i + jump[i] >= n:
                return step_list[i]
            else:
                max_num = max(max_num, i + jump[i])


