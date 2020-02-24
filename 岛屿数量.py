# -*- coding: utf-8 -*-
class Solution:
    # 方向数组，它表示了相对于当前位置的 4 个方向的横、纵坐标的偏移量，这是一个常见的技巧
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


    def numIslands(self, grid: [[str]]) -> int:
        # 暴力法也没啥意思，这个题目还是要用树来完成
        # 这个就是深度优先遍历
        if grid == []:
            return 0
        # 如果结点包含1，就把这个为根节点来深度优先搜索
        m = len(grid)
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        # 构建一个标记矩阵，经过的节点就全都标记一下
        count = 0
        for i in range(m):
            for j in range(n):
                # 只要是陆地，且没有被访问过的，就可以使用 DFS 发现与之相连的陆地，并进行标记
                if not marked[i][j] and grid[i][j] == '1':
                    # count 可以理解为连通分量，你可以在深度优先遍历完成以后，再计数，
                    # 即这行代码放在【位置 1】也是可以的
                    count += 1
                    self.__dfs(grid, i, j, m, n, marked)
                    # 【位置 1】
        return count

    def __dfs(self, grid, i, j, m, n, marked):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                self.__dfs(grid, new_i, new_j, m, n, marked)


# 广度优先遍历也行，加个栈来记录，其实也差不多

print(Solution().numIslands(["11110","11010","11000","00000"]))