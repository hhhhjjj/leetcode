# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 按照节点编号的奇偶性来分，那么就有个n来计数，或者双指针迭代
        # 然后要求用原地算法，和n的时间复杂度
        # 这个链表的数据结构我是真的无语了
        if head is None or head.next is None or head.next.next is None:
            return head
        odd_num = head
        even_num = head.next
        even_head = even_num
        while even_num and even_num.next:
            odd_num.next = even_num.next
            odd_num = odd_num.next
            even_num.next = odd_num.next
            even_num = even_num.next
            # 这个奇数和偶数的一定要一起构造，这样子才不会重复受到影响
        odd_num.next = even_head
        return head

head1 = ListNode(1)
head2 = ListNode(2)
head3 = ListNode(3)
head4 = ListNode(4)
head1.next = head2
head2.next = head3
head3.next = head4
print(Solution().oddEvenList(head1).next.next.val)