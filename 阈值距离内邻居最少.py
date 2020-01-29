# -*- coding: utf-8 -*-
class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold):
        res = []
        # 这个题目从0开始，遍历所有城市，找到城市0到其余所有城市的最短距离，然后找到小于等于阈值的城市个数
        # 然后这样子遍历所有城市，找到里面城市个数最少的城市

print(Solution().findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))

