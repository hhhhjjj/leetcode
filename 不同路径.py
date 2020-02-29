# -*- coding: utf-8 -*-
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 感觉这个题目都不用动态规划也能出来。。
        if m == 0 or n == 0:
            return 0
        dp = [[0] * n] * m
        if m == 1 and n == 1:
            return 1
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

print(Solution().uniquePaths(7, 3))




