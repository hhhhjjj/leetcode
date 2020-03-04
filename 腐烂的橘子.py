# -*- coding: utf-8 -*-
class Solution:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def orangesRotting(self, grid: [[int]]) -> int:
        if grid == [[]]:
            return 0
        # 题目为简单，递归一下应该就行了,我在想要不要记录之前走过的1，省的浪费时间
        max_min = 0
        length_row = len(grid)
        length_col = len(grid[0])
        for i in range(length_row):
            for j in range(length_col):
                if grid[i][j] == 2:
                    self.dfs(i, j ,0)

    def dfs(self, i, j, minutes):
        pass
