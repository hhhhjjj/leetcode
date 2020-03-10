# -*- coding: utf-8 -*-
class Solution(object):
    def myPow(self, x, n):
        # 还是递归，然后用位运算代替乘法，其实位运算的速度也比乘法快
        def func(x, n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            temp = func(x, n >> 1)
            if n & 1: # n为奇数
                return temp * temp * x
            else: # n为偶数
                return temp * temp
        if n >= 0:
            res = func(x, n)
        else:
            res = 1 / func(x, -n)
        return res

    def myPow_2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def func(x, n):
            product = 1
            for _ in range(n):
                product *= x
            return product
        if n >= 0:
            res = func(x, n)
        else:
            res = 1 / func(x, -n)
        return res

print(Solution().myPow(2, -2))