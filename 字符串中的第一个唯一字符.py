# -*- coding: utf-8 -*-
class Solution:
    def firstUniqChar(self, s):
        length = len(s)
        if length < 2:
            return length - 1
        word_dict = {}
        word_position = {}
        for i in range(length):
            if word_dict.get(s[i]):
                word_dict[s[i]] += 1
            else:
                word_dict[s[i]] = 1
                word_position[s[i]] = i
        all_one = filter(lambda x: 1 == x[1], word_dict.items())
        res = length
        for (key, val) in all_one:
            if word_position[key] < res:
                res = word_position[key]
        if res == length:
            return -1
        return res
# 真的是写的慢的一批，直接把出现的次数保存到散列表里面
# 然后再遍历一次字符串，用散列表检查是不是唯一
# 其实两次遍历的时间复杂度也是n，比我这快多了
print(Solution().firstUniqChar("cc"))