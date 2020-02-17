# -*- coding: utf-8 -*-
class ProductOfNumbers:

    def __init__(self):
        # 换成字典比列表还要慢
        self.nums = {0:1}
        self.step = 1

    def add(self, num: int) -> None:
        if num == 0:
            # 在这存储前面所有的乘积，而不是num
            self.nums = {0:1}
            self.step = 1
        #     插入为0的时候，积为0，清空所有，所以还原到最开始的状态
        else:
            self.nums[self.step] = self.nums[self.step - 1] * num
            self.step += 1
        # 因为这个不返回值，所以你内部怎么处理都无所谓的

    def getProduct(self, k: int) -> int:
        # 用这种每次都重新计算的肯定是超时了，在这用前缀和的思想来达到O1的时间复杂度
        # if self.nums:
        #     res = 1
        #     for i in range(self.step - k, self.step):
        #         res *= self.nums[i]
        #     return res
        print(self.step)
        if k >= self.step:
            return 0
        else:
            return int(self.nums[self.step - 1] / self.nums[self.step - 1 - k])

obj = ProductOfNumbers()
obj.add(2)
obj.add(5)
obj.add(4)
param_2 = obj.getProduct(4)
print(param_2)
