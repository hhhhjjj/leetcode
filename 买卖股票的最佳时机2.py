# -*- coding: utf-8 -*-
class Solution:
    def maxProfit(self, prices):
        def profit(prices, i):
            return prices[i + 1] - prices[i]
        res = 0
        length = len(prices)
        if length < 2:
            return 0
        for i in range(length - 1):
            # 就是判断一下利润，只要大于0的都收了，小于0的都不要
            # 其实这个就是贪心算法
            pro = profit(prices, i)
            if pro >= 0:
                res = res + pro
        return res


print(Solution().maxProfit([7,1,5,3,6,4]))


