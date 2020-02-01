# -*- coding: utf-8 -*-
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        word_dict = {}
        for i in s:
            if word_dict.get(i):
                word_dict[i] += 1
            else:
                word_dict[i] = 1
        for i in t:
            if word_dict.get(i):
                word_dict[i] -= 1
                if word_dict[i] == 0:
                    word_dict.pop(i)
            else:
                return False
        if word_dict != {}:
            return False
        return True
# 这个可以直接两个字符串来排序判断就行
# 或者直接使用内置的计数器
# 如果数据量再大，就用哈希表

print(Solution().isAnagram("ab", "a"))