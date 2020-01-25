# -*- coding: utf-8 -*-
class Solution:
    def arrayRankTransform(self, arr):
        length = len(arr)
        if length == 0:
            return None
        import copy
        arr1 = copy.deepcopy(arr)
        # 要去重，不然序列会是错的
        # 注意列表深拷贝
        arr1.sort()
        res = []
        for i in range(length):
            res.append(arr1.index(arr[i]) + 1)
        return res


print(Solution().arrayRankTransform([37,12,28,9,100,56,80,5,12]))



