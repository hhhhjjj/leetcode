# -*- coding: utf-8 -*-
class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        if nums == []:
            return [[]]
        # 肯定是不调库的itertools.permutations
        res = []
        # 看题解还是用回溯法，其实就是递归

        def backtrack(nums, tmp):
            length = len(nums)
            if not nums:
                res.append(tmp)
            else:
                # 因为每次传进来的length不一样，所以需要重新算长度
                for i in range(length):
                    backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res

print(Solution().permute([1,2,3]))




