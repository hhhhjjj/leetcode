# -*- coding: utf-8 -*-
class Solution:
    def getTriggerTime(self, increase: [[int]], requirements: [[int]]) -> [int]:
        # 这里用一个前缀和不行，要用三个记录才比较快
        n, r = len(increase), len(requirements)
        preSum_c, preSum_r, preSum_h = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
        res = [-1] * r

        for i in range(n):
            preSum_c[i + 1] = preSum_c[i] + increase[i][0]
            preSum_r[i + 1] = preSum_r[i] + increase[i][1]
            preSum_h[i + 1] = preSum_h[i] + increase[i][2]
        for i in range(r):
            left, right = 0, n
            while left <= right:
                # 这里用了个二分查找
                mid = left + (right - left) // 2
                if preSum_c[mid] >= requirements[i][0] and preSum_r[mid] >= requirements[i][1] and preSum_h[mid] >= \
                        requirements[i][2]:
                    res[i] = mid
                    right = mid - 1
                else:
                    left = mid + 1
        return res

print(Solution().getTriggerTime(increase = [[0,4,5],[4,8,8],[8,6,1],[10,10,0]],requirements = [[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]]))