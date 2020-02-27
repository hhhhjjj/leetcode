# -*- coding: utf-8 -*-
class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        length = len(nums)
        if length < 1:
            return [nums]
        # 还是没想到什么好办法，除了调库
        # 迭代就感觉是n方级别了
        res = []
        # from itertools import combinations
        # for i in range(length + 1):
        #     for tmp in combinations(nums, i):
        #         # 这个返回的是个list
        #         res.append(tmp)
        # return res
        # 在这用回溯，其实就是排列组合
        def helper(i, tmp):
            res.append(tmp)
            # 这个i是每一层
            for j in range(i, length):
                helper(j + 1, tmp + [nums[j]])
        #         每次在这加上一位后面的，这个方法也挺好
        helper(0, [])
        return res
#     在这研究下如何回溯
# 对于答案更新，我们考虑选还是不选当前答案
# 在这就是每一层都考虑当前的值我们是要还是不要
# 我们不需要用遍历，但是又要对不同index进行判断，那么我们就传入一个index变量进去，每次改变index就可以了，用于指向每个元素

print(Solution().subsets([1,2,3]))