# -*- coding: utf-8 -*-
class Solution:
    def isPossible(self, target: [int]) -> bool:
        # 比赛中没做出来，看的题解用的倒推的方法
        # 数组中最大的数是当前的x，所有数的和减去这个最大数，就是这次和上次的增量
        while True:
            current_x = max(target)
            if current_x == 1:
                return True  # 最大的数等于 1 了而且数组中无小于 1 的数，那么说明整个数组都是 1，返回 True
            idx = target.index(current_x)
            # 得到索引
            s = sum(target)
            inc = s - current_x
            # 得到增量
            if inc >= current_x:
                return False  # inc 大于等于 x，这样将会出现小于 1 的值，不是合法情况，返回 False
            target[idx] = current_x % inc
            # 用取余比减号要快些
