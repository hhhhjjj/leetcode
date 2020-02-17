# -*- coding: utf-8 -*-
class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = nums1[:m]
        # nums1_max = nums1[-1]
        # if nums2:
        #     if nums1[-1] <= nums2[0]:
        #         nums1.extend(nums2)
        #     elif nums2[-1] <= nums1[0]:
        #         nums2.extend(nums1)
        #         nums1 = nums2
        #     else:
        #         nums1_cur = 0
        #         nums2_cur = 0
        #         while nums2_cur < n:
        #             if nums1[nums1_cur] < nums2[nums2_cur]:
        #                 if nums1[nums1_cur] == nums1_max:
        #                     nums1.extend(nums2[nums2_cur:])
        #                     break
        #                 nums1_cur += 1
        #
        #             else:
        #                 nums1.insert(nums1_cur, nums2[nums2_cur])
        #                 nums1_cur += 1
        #                 nums2_cur += 1
        # print(nums1)
        # 不知道为什么我这个本机上运行没问题，但是leetcode上就直接返回了初始的nums1
        nums1_copy = nums1[:m]
        nums1[:] = []

        # Two get pointers for nums1_copy and nums2.
        p1 = 0
        p2 = 0

        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # if there are still elements to add
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]


print(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3))
