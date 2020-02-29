# -*- coding: utf-8 -*-
class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix != [[]]:
            length_row = len(matrix)
            length_col = len(matrix[0])
            # 暴力法太蠢。还是把行列都记住再换
            col_0 = set()
            row_0 = set()
            for row in range(length_row):
                for col in range(length_col):
                    if matrix[row][col] == 0:
                        col_0.add(col)
                        row_0.add(row)
            for col in col_0:
                for row in range(length_row):
                    matrix[row][col] = 0
            for row in row_0:
                matrix[row] = [0]*length_col
            # 这方法消耗了m + n的空间复杂度
            # 其实可以改成直接用第一行和列来保存是否换成0，这样子就不需要额外的set了



print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))






