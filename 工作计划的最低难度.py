# -*- coding: utf-8 -*-
class Solution:
    def minDifficulty(self, jobDifficulty, d):
        length = len(jobDifficulty)
        if length < d or d == 0 or length == 0:
            return -1
        if length == d:
            return sum(jobDifficulty)
        res = 0
        # 这里有个条件是要执行第i项必须完成前面全部的
        

print(Solution().minDifficulty(jobDifficulty = [6,5,4,3,2,1], d = 2))