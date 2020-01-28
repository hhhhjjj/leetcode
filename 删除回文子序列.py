# -*- coding: utf-8 -*-
class Solution:
    def removePalindromeSub(self, s):
        # 最先想到可以先找到里面有多少个回文子序列，这样就直接出结果了
        length = len(s)
        if length < 2:
            return length
        # 其实这题目只有a和b，反正是子序列，可以一步删所有a，一步所有b
        # 或者删整体是回文的
        if s == s[::-1]:
            return 1
        return 2



print(Solution().removePalindromeSub("ababb"))