# -*- coding: utf-8 -*-
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        # 这个题直接层次遍历找到每一层的所有节点，然后来指就行了
        res = []

        def helper(root,depth):
            if root:
                try:
                    res[depth].append(root)
                except:
                    res.append([root])
                depth += 1
                helper(root.left, depth)
                helper(root.right, depth)
        helper(root, 0)
        for i in range(len(res)):
            for j in range(len(res[i])):
                if j == len(res[i]) - 1:
                    res[i][j].next = None
                else:
                    res[i][j].next = res[i][j + 1]
        return root

# 这种方法消耗了额外的空间，还可以不用额外空间的
# 第 N 层节点之间建立 next 指针后，再建立第 N+1 层节点的 next 指针。可以通过 next 指针访问同一层的所有节点，因此可以使用第 N 层的 next 指针，为第 N+1 层节点建立 next 指针
# 而且这样子时间也节省了