# -*- coding: utf-8 -*-
class Solution:
    def removePalindromeSub(self, s):
        # 感觉可以先找到里面有多少个回文子序列，这样就直接出结果了
        length = len(s)
        if length < 2:
            return length
        left = 0
        right = length - 1
        res = 1
        while left <= right:
            if s[left] == s[right]:
                left = left + 1
                right = right - 1
            else:
                if s[left + 1] == s[right]:
                    left = left + 1
                    res = res + 1
                elif s[left] == s[right - 1]:
                    right = right - 1
                    res = res + 1
        return res


print(Solution().removePalindromeSub("ababb"))