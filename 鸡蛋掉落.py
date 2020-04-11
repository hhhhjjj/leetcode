# -*- coding: utf-8 -*-
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # 这题目就是求最小次数，感觉应该是动态规划来做
        # 这个F = 0的时候也会碎掉，也就是说其实一共是N + 1层
        # 在第x层楼扔鸡蛋，这个x取中间值就行
        # 如果鸡蛋不碎。状态变成（k, n - x)
        # 如果碎了就是k - 1，x - 1
        # 因为要选最坏情况中的最小值
        # 所以就是min(max(dp[k - 1][n - 1], dp[k][n- x]) + 1)
        # 然后再优化这些
        memo = dict()

        def dp(K, N):
            if K == 1: return N
            if N == 0: return 0
            if (K, N) in memo:
                return memo[(K, N)]

            res = float('INF')
            # 用二分搜索代替线性搜索
            lo, hi = 1, N
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(K - 1, mid - 1)  # 碎
                not_broken = dp(K, N - mid)  # 没碎
                # res = min(max(碎，没碎) + 1)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)

            memo[(K, N)] = res
            return res

        return dp(K, N)
