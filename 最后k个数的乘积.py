# -*- coding: utf-8 -*-
class ProductOfNumbers:

    def __init__(self):
        # 换成字典看看
        self.nums = {}
        self.step = 0

    def add(self, num: int) -> None:
        self.nums[self.step] = num
        self.step += 1

    def getProduct(self, k: int) -> int:
        if self.nums:
            res = 1
            for i in range(self.step - k, self.step):
                res *= self.nums[i]
            return res
# 一直超时
