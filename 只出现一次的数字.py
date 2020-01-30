# -*- coding: utf-8 -*-
class Solution:
    def singleNumber(self, nums):
        length = len(nums)
        if length == 1:
            return nums[0]
        # n的时间复杂度，还不用额外空间
        # 也就是说不能用哈希表来节省时间
        # 我想的是先排序，然后再来遍历一次，但是不符合要求
        # 看了题解才知道是用位运算来完成的
        # 对0和二进制位异或得到的是这个二进制位，相同的二进制异或返回是0
        # 所以对所有数异或，就可以得到唯一的数字了
        res = 0
        for i in nums:
            res ^= i
        return res
