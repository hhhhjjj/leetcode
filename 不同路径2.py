# -*- coding: utf-8 -*-
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        # 之前是用的动态规划直接出来的
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 0 or n == 0:
            return 0
        dp = [[0]* n for i in range(m)]
        # 就这样子生成才对
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j == 0:
                        if obstacleGrid[i][j] == 0:
                            dp[i][j] = 1
                        else:
                            return 0
                    else:
                        if obstacleGrid[i][j] == 0 and dp[i][j-1] != 0:
                            dp[i][j] = 1
                elif j == 0:
                    if obstacleGrid[i][j] == 0 and dp[i-1][j] != 0:
                        dp[i][j] = 1
                else:
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # print(dp)
        return dp[-1][-1]


print(Solution().uniquePathsWithObstacles([[1,0]]
))