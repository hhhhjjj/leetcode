# -*- coding: utf-8 -*-
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 这个题目确实没想出来如何就地操作，想的是先复制一下
        # 先转置矩阵，然后翻转每一行其实就可以了
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for i in range(n):
            matrix[i].reverse()


# 还可以更加简略，原地旋转不代表不可以用额外空间，用常量空间还是可以的
# 其实就是构造成四个矩阵来转就行





