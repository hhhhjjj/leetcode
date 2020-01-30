# -*- coding: utf-8 -*-
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 0:
            pass
        else:
            cur = 0
            zero_num = 0
            temp = [0]
            while True:
                if nums[cur] == 0:
                    nums.pop(cur)
                    zero_num += 1
                    nums.extend(temp)
                    if cur == length - zero_num:
                        break
                else:
                    if cur == length - zero_num - 1:
                        break
                    cur += 1
            return nums

# 慢的一批，这种只能在原数组上操作的其实可以用双指针
# 当然这还不是最优的，如果只有一个非零的在最后面，还是前面要写一大堆
# 当我们遇到一个非零元素时，我们需要交换当前指针和慢速指针指向的元素，然后前进两个指针。如果它是零元素，我们只前进当前指针。

print(Solution().moveZeroes([1]))