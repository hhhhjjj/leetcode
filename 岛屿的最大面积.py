# -*- coding: utf-8 -*-
class Solution:
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        # 这个用优先搜索吧
        length_row = len(grid)
        if length_row == 0:
            return 0
        length_col = len(grid[0])
        # dp = [[False] * length_col] * length_row
        # 这里构造这个dp不能用乘法，采用的是浅拷贝，会全部改变,还是要用for循环来
        dp = [[(False) for i in range(length_col)] for _ in range(length_row)]
        res = 0
        steps = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def helper(row_in, col_in, res_in):
            for step in steps:
                if 0 <= row_in + step[0] <= length_row - 1 and 0 <= col_in + step[1] <= length_col - 1 and grid[row_in + step[0]][col_in + step[1]] == 1 and dp[row_in + step[0]][col_in + step[1]] is False:
                    dp[row_in + step[0]][col_in + step[1]] = True
                    res_in += helper(row_in + step[0], col_in + step[1], 1)
            return res_in

        for row in range(length_row):
            for col in range(length_col):
                if grid[row][col] == 1 and dp[row][col] is False:
                    dp[row][col] = True
                    res = max(res, helper(row, col, 1))
        return res


print(Solution().maxAreaOfIsland([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))


