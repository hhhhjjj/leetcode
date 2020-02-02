# -*- coding: utf-8 -*-
class Solution:
    def strStr(self, haystack, needle):
        length1 = len(haystack)
        length2 = len(needle)
        if length1 < length2:
            return -1
        if length2 == 0:
            # 为空的时候返回0
            return 0
        cur = 0
        while cur <= length1 - length2:
            if haystack[cur] == needle[0]:
                if haystack[cur:cur + length2] == needle:
                    return cur
            cur += 1
        return -1
# 也可以直接用自带的find来找
print(Solution().strStr("hell", "ll"))