# -*- coding: utf-8 -*-
class Solution:

    def __init__(self, nums: [int]):
        self.nums = nums
        self.original = nums
        self.length = len(nums)

    def reset(self) -> [int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.original
        return self.nums

    def shuffle(self) -> [int]:
        """
        Returns a random shuffling of the array.
        """
        # 直接用random了
        import random
        return random.sample(self.nums, self.length)


print(Solution([1,2,3]).shuffle())