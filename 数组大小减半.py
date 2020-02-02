# -*- coding: utf-8 -*-
class Solution:
    def minSetSize(self, arr):
        length = len(arr)
        set_arr = set(arr)
        if len(set_arr) == 1:
            return 1
        from collections import Counter
        counter_num = Counter(arr).most_common()
        res = 0
        for i in range(length):
            res += counter_num[i][1]
            if res >= length /2:
                return i + 1

print(Solution().minSetSize([3,3,3,3,5,5,5,2,2,7]))