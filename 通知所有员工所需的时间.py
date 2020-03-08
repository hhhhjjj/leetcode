# -*- coding: utf-8 -*-
# 这个感觉是用树来完成，但是不知道如何不扫描那么多次manger
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: [int], informTime: [int]) -> int:
        if n <= 1:
            return 0
        manager_dict = {}
        for i in range(n):
            if manager_dict.get(manager[i]):
                manager_dict[manager[i]].append(i)
            else:
                manager_dict[manager[i]] = [i]
        print(manager_dict)
        self.res = 0
        def helper(ls):
            max_time = 0
            for i in ls:
                if informTime[i] > max_time:
                    max_time = informTime[i]
                if manager_dict.get(i):
                    helper(manager_dict[i])
            self.res += max_time
        helper(manager_dict[-1])
        return self.res



print(Solution().numOfMinutes(n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))