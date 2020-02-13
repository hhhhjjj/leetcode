# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 用列表之类的方法就不说了
        # 在这用双指针迭代
        pre = None
        cur = head
        while cur:
            # 链表的题目一般都不改动原链表，用额外空间来
            temp = cur.next
            cur.next = pre
            # 在这都前进一位
            pre = cur
            cur = temp
        return pre