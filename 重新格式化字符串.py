# -*- coding: utf-8 -*-
class Solution:
    def reformat(self, s: str) -> str:
        # 这个直接来个东西存储就完事了，只是想着怎么优化时间复杂度而已
        d = ''
        p = ''
        res = ""
        for i in s:
            if i.isalpha():
                d += i
            else:
                p += i
        if len(d) == len(p) + 1:
            for i in range(len(p)):
                res += d[i]
                res += p[i]
            res += d[-1]
        if len(d) == len(p) - 1:
            for i in range(len(d)):
                res += p[i]
                res += d[i]
            res += p[-1]
        if len(d) == len(p):
            for i in range(len(d)):
                res += p[i]
                res += d[i]
        return res