# -*- coding: utf-8 -*-
class Solution:
    def diagonalSort(self, mat):
        all_row = len(mat)
        # 行起点的对角线是all_row - 1,列起点的对角线是all_col - 2
        all_col = len(mat[0])
        res = mat
        # 行和列分别来
        for row in range(all_row - 1):
            # 记录最开始的位置，因为后面会发生改变
            row_init = row
            col = 0
            temp = []
            while row < all_row and col < all_col:
                temp.append(mat[row][col])
                row = row + 1
                col = col + 1
            temp.sort()
            col = 0
            while temp:
                res[row_init][col] = temp.pop(0)
                row_init = row_init + 1
                col = col + 1

        for col in range(1, all_col - 1):
            col_init = col
            row = 0
            temp = []
            while row < all_row and col < all_col:
                temp.append(mat[row][col])
                row = row + 1
                col = col + 1
            temp.sort()
            row = 0
            while temp:
                res[row][col_init] = temp.pop(0)
                row = row + 1
                col_init = col_init + 1
        return res

print(Solution().diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))




