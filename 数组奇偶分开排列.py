# -*- coding: utf-8 -*-
# n长度数组，有奇数有偶数，需要奇数在前，偶数在后排列，需要稳定！！！
# 当然这个题目可以时间复杂度为n
class Solution:
    def ls_sort(self, ls):
        # 肯定是弄一次遍历，至于空间复杂度再去优化吧
        # 这个其实感觉就是插入排序
        length = len(ls)
        odd_flag = 0
        for i in range(length):
            if ls[i] % 2:
                if i != odd_flag:
                    tmp = ls[i]
                    ls.pop(i)
                    ls.insert(odd_flag, tmp)
                odd_flag += 1
        return ls
# 感觉我还行啊，一步到位



print(Solution().ls_sort([1,4,3,5,7,8,2]))
