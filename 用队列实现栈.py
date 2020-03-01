# -*- coding: utf-8 -*-
from queue import Queue
# 直接调用个基本的fifo队列出来
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_queue = Queue()
        # 一个是肯定不能完成的，需要两个
        # 出栈其实也没啥技巧，就是循环一遍倒过来而已
        #     put插入，get直接出来一个最先进去的
        self.top_num = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.my_queue.put(x)
        self.top_num = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        length = self.my_queue.qsize()
    #     这个不支持len，需要用自带的得到长度的
        cur = 1
        while cur <= length - 1:
            self.top_num = self.my_queue.get()
            self.my_queue.put(self.top_num)
            cur += 1
        return self.my_queue.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.top_num

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.my_queue.empty()