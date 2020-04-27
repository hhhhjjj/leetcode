# -*- coding: utf-8 -*-
class Solution:
    def fib(self, n):
        # 三种解题方法
        if n == 1:
            return 1
        if n == 0:
            return 0
        res_init = 0
        res_first = 1
        res_second = 0
        for i in range(2, n + 1):
            res_second = res_init + res_first
            res_init = res_first
            res_first = res_second
        return res_second

        # if n == 0:
        #     return 0
        # if n == 1 or n == 2:
        #     return 1
        # return self.fib(n - 1) + self.fib(n - 2)