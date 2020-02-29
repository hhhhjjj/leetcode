# -*- coding: utf-8 -*-
class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        # 这个暴力递归肯定超时，其实还是动态规划，
        # 最少一元钱，所以最多也就amount 加一次
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        print(dp)
        for i in range(1, amount + 1):
            # 这里正好每个index代表了对应的值
            for j in range(len(coins)):
                # 在这试一下每一个值
                if i >= coins[j]:
                    # 这个硬币我选择拿还是不拿
                    # 其实当前的值都是1元叠上去的，所以基本都比拿的要大
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        return -1 if dp[-1] == amount + 1 else dp[-1]

print(Solution().coinChange(coins = [1,2,5], amount = 11))