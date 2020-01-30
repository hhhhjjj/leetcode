# -*- coding: utf-8 -*-
class Solution:
    def minDifficulty(self, jobDifficulty, d):
        length = len(jobDifficulty)
        if length < d or d == 0 or length == 0:
            return -1
        if length == d:
            return sum(jobDifficulty)
        res = 0
        # 用动态规划来解还是比较稳的，复杂度为dn方


print(Solution().minDifficulty(jobDifficulty = [6,5,4,3,2,1], d = 2))