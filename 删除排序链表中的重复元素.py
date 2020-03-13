# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        cur = head
        while cur.next is not None:
            if cur.next.val != cur.val:
                cur = cur.next
            else:
                tmp = cur.next.next
                cur.next = tmp
        return head

L1 = ListNode(1)
L2 = ListNode(1)
L3 = ListNode(2)
L1.next = L2
L2.next = L3
print(Solution().deleteDuplicates(L1).next.val)