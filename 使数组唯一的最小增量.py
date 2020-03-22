# -*- coding: utf-8 -*-
class Solution:
    def minIncrementForUnique(self, A: [int]) -> int:
        if A == []:
            return 0
        A.sort()
        res = 0
        for i in range(1, len(A)):
            if A[i] <= A[i-1]:
                res += A[i-1] + 1 - A[i]
                A[i] = A[i-1] + 1
        return res


print(Solution().minIncrementForUnique([3,2,1,2,1,7]))




