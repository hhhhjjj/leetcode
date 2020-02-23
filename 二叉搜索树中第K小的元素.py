# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 二叉搜索树就是左边总是比中间小，比右边更小的
        # 我想的是直接把所有的都遍历出来，然后找K
        # 但是这样子没啥技术含量，发现题解基本都是这样
        # 在这用迭代的话会比递归快，迭代只需要在找到答案后就停止了
        # 这个是二叉搜索树，用中序遍历正好是排序了的
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
                # 左边到头的必然是最小的
            root = stack.pop()
            # 放在这就不用担心会回左边了
            k -= 1
            if k == 0:
                # 这里要求返回的是值而不是节点
                return root.val
            root = root.right


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

Tree = createtree([5,3,6,2,4,None,None,1])
print(Solution().kthSmallest(Tree, 3))



