# -*- coding: utf-8 -*-
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        cur = length - 1 - 1
        if length >= 2:
            while True:
               s.append(s[cur])
               s.pop(cur)
               if cur == 0:
                   break
               else:
                   cur -= 1
        return s
# 慢的一批，直接双指针序号位置交换就是了
print(Solution().reverseString(["h","e","l","l","o"]))


