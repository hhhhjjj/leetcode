# -*- coding: utf-8 -*-
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: [int], informTime: [int]) -> int:
        res = 0
        for i in range(n):
            if informTime[i] == 0:
                temp = 0
                index = i
                while index != - 1:
                    temp += informTime[index]
                    index = manager[index]
                res = max(res, temp)
        # 这个就是根据现有数据从下往上推，然后用res来去重
        return res



print(Solution().numOfMinutes(n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))