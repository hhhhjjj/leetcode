# -*- coding: utf-8 -*-
class Solution:
    def minTaps(self, n, ranges):
        if n == 0:
            return 1
        length = n + 1
        res = 0
        min_right = 0
        max_left = 0
        # 在这的想法是可以用两遍循环，第一个把小范围的都删了，第二个循环就是判断能不能覆盖所有
        for i in range(length):
            if ranges[i] == 0:
                continue
            if i - ranges[i] <= 0 and i + ranges[i] >= n:
                return 1
            if i - ranges[i] < min_right:
                min_right = i - ranges[i]
                res = res + 1
            if i + ranges[i] > max_left:
                res = res + 1
                max_left = i - ranges[i]
            if min_right <= 0 and max_left >= n:
                return res
        return -1


print(Solution().minTaps(5, [3,4,1,1,0,0]))



