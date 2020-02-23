# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def createtree(l):
    if l[0]:
        root = TreeNode(l[0])
        nodes = [root]
        id = 1
        while nodes and id < len(l):
            node = nodes[0]  # 依次为每个节点分配子节点
            node.left = TreeNode(l[id]) if l[id] else None
            nodes.append(node.left)
            node.right = TreeNode(l[id + 1]) if id < len(l) - 1 and l[id + 1] else None
            nodes.append(node.right)
            id += 2  # 每次取出两个节点
            nodes.pop(0)
        return root
    else:
        return None