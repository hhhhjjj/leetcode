# -*- coding: utf-8 -*-
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.min_num = []

    def push(self, x: int) -> None:
        self.nums.append(x)
        self.min_num.append(x)
        self.min_num.sort()

    def pop(self) -> None:
        # 如果把之前的最小值删了的话
        # 后面再求最小值就不能用之前的这个了
        # 所以插入的时候就应该排序
        self.min_num.remove(self.nums[-1])
        self.min_num.sort()
        self.nums.pop()

    def top(self) -> int:
        # 栈顶指的是最后一个数
        return self.nums[-1]

    def getMin(self) -> int:
        return self.min_num[0]

# 题解比我的好很多，也是用辅助栈，但是辅助栈是用来存放最小数的，不需要我这样子每次排序