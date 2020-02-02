# -*- coding: utf-8 -*-
class Solution:
    def kWeakestRows(self, mat, k):
        length = len(mat)
        res = []
        for i in range(length):
            res.append(sum(mat[i]))
        index = sorted(enumerate(res), key=lambda x: x[1])
        res1 = []
        for i in range(k):
            res1.append(index[i][0])
        return res1


print(Solution().kWeakestRows(mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2))