# -*- coding: utf-8 -*-
class Solution:
    def countNegatives(self, grid: [[int]]) -> int:
        length_row = len(grid)
        if length_row == 0:
            return 0
        length_col = len(grid[0])
        res = 0
        for i in range(length_row):
            for j in range(length_col):
                if grid[i][j] < 0:
                    res += length_col - j
                    break
        return res

print(Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))