# -*- coding: utf-8 -*-
class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold):
        res = []
        city_dict = {}
        for i in range(n):
            city_dict[i] = 0
        # for i in range(n):
        #     if edges[i][2] <= distanceThreshold:
        #         city_dict[edges[i][0]] = city_dict[edges[i][0]] + 1
        #         city_dict[edges[i][1]] = city_dict[edges[i][1]] + 1
        # print(city_dict)

print(Solution().findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))

