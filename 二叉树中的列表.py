# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root:
            return False
        # 这个树的话用的应该是深度优先遍历
        def dfs(head, root):
            if head is None:
                return True
            if root is None:
                return False
            if root.val == head.val:
                # 要注意这个链表中间不能断，断了就要重新开始,但是我看题解这里断了就直接没了
                return dfs(head.next,root.left) or dfs(head.next, root.right)
            else:
                return False
        return dfs(head,root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
# 这左右两个需要从头考虑，而且这个也在递归里面，所以断了也无所谓

print(Solution().isSubPath())