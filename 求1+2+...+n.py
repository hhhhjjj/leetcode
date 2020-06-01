# -*- coding: utf-8 -*-
class Solution:
    # def sumNums(self, n: int) -> int:
    #     # # 这不就是个等差数列嘛,但是不能用乘除法。。。
    #     # return int((1 + n) * n / 2)
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        # 这里用短路运算符来终止递归
        self.res += n
        return self.res
