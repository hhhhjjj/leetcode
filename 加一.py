# -*- coding: utf-8 -*-
class Solution:
    def plusOne(self, digits):
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            digits[-1] = 0
            if len(digits) == 1:
                return [1,0]
            cur = len(digits) - 2
            while True:
                digits[cur] += 1
                if digits[cur] == 10:
                    digits[cur] = 0
                    if cur == 0:
                        res = [1]
                        res.extend(digits)
                        return res
                    cur -= 1
                else:
                    break
            return digits
# 这个算法真的是慢的一批
# 感觉还是可以再优化一下过程

print(Solution().plusOne([9, 9]))
