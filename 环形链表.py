# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 记得这种判断环的就快慢指针一直跑下去遇到相同的就行了
        if head is None or head.next is None or head.next.next is None:
            return False
        fast_cur = head.next.next
        slow_cur = head.next
        while True:
            try:
                if fast_cur.val != slow_cur.val:
                    fast_cur = fast_cur.next.next
                    slow_cur = slow_cur.next
                else:
                    return True
            except:
                return False

# 慢的一批，

