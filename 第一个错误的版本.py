# -*- coding: utf-8 -*-
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 这个感觉是二分查找了
        return helper(1, n)

def helper(start, end):
    # 其实我觉得可以用字典记录下来搜索过的答案，这样子就能减少后面调用api的次数
    if (end + start)//2 > 1:
        if isBadVersion((end + start)//2) and isBadVersion((end + start)//2 - 1) is False:
            return (end + start)//2
        elif isBadVersion((end + start)//2) and isBadVersion((end + start)//2 - 1) is True:
            return helper(start, (end + start)//2)
        elif isBadVersion((end + start)//2) is False:
            if isBadVersion((end + start) // 2 + 1):
                return (end + start) // 2 + 1
            return helper((end + start)//2, end)
    else:
        if isBadVersion((end + start) // 2) is False:
            return 2
        else:return 1


def isBadVersion(version):
    # print(version)
    if version > 3:
        return True
    else:
        return False


print(Solution().firstBadVersion(5))