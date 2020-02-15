# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            # 空链表也算回文
            return True
        if head.next == None:
            return True
        # 因为是要求1的空间复杂度，就不能用栈，在这是用双指针来解决的
        # 这种问题可以用快慢指针找到链表中间，然后反转链表后半部分，来和前半部分对比
            # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous





head1 = ListNode(0)
head2 = ListNode(0)
head1.next = head2
print(Solution().isPalindrome(head1))