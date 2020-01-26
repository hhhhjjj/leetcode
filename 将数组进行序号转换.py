# -*- coding: utf-8 -*-
class Solution:
    def arrayRankTransform(self, arr):
        length = len(arr)
        import copy
        arr1 = list(set(copy.copy(arr)))
        # 要去重，不然序列会是错的
        # 注意列表深拷贝
        arr1.sort()
        index_dict = dict(zip(arr1,range(len(arr1))))
        res = []
        for i in range(length):
            res.append(index_dict[arr[i]] + 1)
        return res


print(Solution().arrayRankTransform([37,12,28,9,100,56,80,5,12]))



