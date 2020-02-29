# -*- coding: utf-8 -*-
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 需要时间复杂度为logn，也就是说二分来解决
        # 要想有0，那么就需要2乘以5,其实就是看有几个5，毕竟2的数量很多
        res = 0
        while n>=5:
            res += n//5
            n = n//5
        return res
# 这么慢。。。

print(Solution().trailingZeroes(25))