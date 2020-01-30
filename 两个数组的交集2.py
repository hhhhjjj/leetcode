# -*- coding: utf-8 -*-
class Solution:
    def intersect(self, nums1, nums2):
        length1 = len(nums1)
        length2 = len(nums2)
        if length1 == 0 or length2 == 0:
            return []
        # 把一个存到哈希表，另外一个来查询
        nums1_dict = {}
        for i in range(length1):
            if nums1_dict.get(nums1[i]):
                nums1_dict[nums1[i]] += 1
            else:
                nums1_dict[nums1[i]] = 1
        res = []
        for i in range(length2):
            if nums1_dict.get(nums2[i]):
                res.append(nums2[i])
                nums1_dict[nums2[i]] -= 1
                if nums1_dict[nums2[i]] == 0:
                    nums1_dict.pop(nums2[i])
        return res
# 如果是排序的列表双指针就解决了

# 如果内存十分小的，数据十分大
# 那么就不能用哈希了，浪费空间
# 归并排序就是和外部打交道的
# 用归并排序，小文件合并到大文件

