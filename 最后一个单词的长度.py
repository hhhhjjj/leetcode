# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == "":
            return 0
        # 感觉这题目直接逆序来不就行了
        # 看了下题解，有的直接找最后一个空格所在的索引
        res = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                res += 1
            else:
                if res != 0:
                    return res
        return res

print(Solution().lengthOfLastWord("H "))