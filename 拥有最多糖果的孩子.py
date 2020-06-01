# -*- coding: utf-8 -*-
class Solution:
    def kidsWithCandies(self, candies: [int], extraCandies: int) -> [bool]:
        # 这个直接得到最大值，然后再遍历一遍来相加
        maxCandies = max(candies)
        ret = [candy + extraCandies >= maxCandies for candy in candies]
        return ret



