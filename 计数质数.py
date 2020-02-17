# -*- coding: utf-8 -*-
class Solution:
    def countPrimes(self, n: int) -> int:
        # if n < 3 :
        #     return 0
        # res = 1
        # for i in range(n):
        #     for j in range(2, int(i**0.5) + 1):
        #         # 这种n方时间复杂度的容易超时
        #         # 在这的j其实不需要遍历到一半，只需要遍历到根号i就行,因为后面的都是反过来的
        #         # 当然其实还有更快的方法
        #         if (i % j) == 0:
        #             break
        #         else:
        #             if j == i//2 + 1:
        #                 res += 1
        # return res
#     直接用排除法，从2开始筛选，最后留下的是质数
        if n < 2:
            return 0

        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0  # 0和1不是质数，先排除掉

        # 埃式筛，把不大于根号n的所有质数的倍数剔除
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(isPrime)


print(Solution().countPrimes(10))

