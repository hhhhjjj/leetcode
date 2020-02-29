# -*- coding: utf-8 -*-
class Solution:
    def leastInterval(self, tasks: [str], n: int) -> int:
        if tasks == []:
            return 0
        length = len(tasks)
        if n == 0:
            return length
        from collections import Counter
        nums = Counter(tasks)
        # 看了题解和我一样，先计数排序
        # 至少需要的最少时间,就是正好把所有的都包含进去了
        max_num= nums.most_common(1)[0][1]
        # 这个返回的是列表，然后里面还是个元组
        res = (max_num - 1) * (n + 1)
        for num in nums:
            # 如果和最大数次数相等的话，就说明包不进去，还需要外面额外加
            if nums[num] == max_num:
                res += 1
        return res if res >= length else length
# 这里要注意为n比较小的时候，反正都是取大的数

print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2
))