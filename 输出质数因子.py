# -*- coding: utf-8 -*-
# 给定一个正整数，按照从小到大输出所有质数因子
# 质数因子不是质数，这个是整数的因式分解
# 比如180输出的是2,2,3,3,5这样子的
class Solution:
    # 1没有质数因子
    def putput_prime(self, num):
        tmp = 2
        res = []
        if num == tmp:
            res.append(num)
            return res
        while num >= tmp:
            remainder = num % tmp
            if remainder == 0:
                res.append(tmp)
                num = num / tmp
            else:
                tmp += 1
        return res

print(Solution().putput_prime(180))





