# -*- coding: utf-8 -*-
# 这个题目直接随便写个
class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 0:
            return ""
        if n% 2 == 0:
            return "x" * (n - 1) + "y"
        else:
            return "x" * (n)

print(Solution().generateTheString(3))