# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        else:
            # 感觉这个题目直接用个哈希表就完事了
            # 看了下题解是这样，但是空间复杂度为其中一部分，这时候想着优化，把空间复杂度变成1
            # 在这用双指针，其实还是构造一个环
            # 这里还需要将B的末位连在A的头上
            # 这样子才能够根据差值来找到
            # 1 3+5 6 3
            # 5 6 3 + 1 3
            # 就判断最后就行
            curA = headA
            curB = headB
            while True:
                if curA == curB:
                    return curA
                if curA is None:
                    curA = headB
                else:
                    curA = curA.next
                if curB is None:
                    curB = headA
                else:
                    curB = curB.next
