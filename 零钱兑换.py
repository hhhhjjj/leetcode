# -*- coding: utf-8 -*-
class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        # 不能直接用1，2，3，4这样子，因为不能确定coins里面是不是有1
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


print(Solution().coinChange(coins = [1, 2, 5], amount = 11))

