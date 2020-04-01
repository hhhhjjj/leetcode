# -*- coding: utf-8 -*-
class Solution:
    def judgePoint24(self, nums: [int]) -> bool:
        # 这个应该就是用回溯了
        # 取数加递归加剪枝
        if not nums: return False

        def helper(nums):
            # if len(nums) == 1: return nums[0] == 24
            # 上面这个还不行，要用下面这个，主要是因为可能会算出来小数，比如23.99999这种
            if len(nums) == 1:
                return abs(nums[0]-24) < 1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        newnums = [nums[k] for k in range(len(nums)) if i != k != j]
                        # 取出i和j位置之外剩下的数
                        # 剩下两个位置进行运算
                        if helper(newnums + [nums[i] + nums[j]]): return True
                        if helper(newnums + [nums[i] - nums[j]]): return True
                        if helper(newnums + [nums[i] * nums[j]]): return True
                        if nums[j] != 0 and helper(newnums + [nums[i] / nums[j]]): return True
            return False

        return helper(nums)





print(Solution().judgePoint24([3,3,8,8]))