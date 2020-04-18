# -*- coding: utf-8 -*-
class Solution:
    def minCount(self, coins: [int]) -> int:
        # 我感觉这个就贪心算法
        res = 0
        for coin in coins:
            res += coin // 2 + coin % 2
        return res


print(Solution().minCount([4,2,1]))