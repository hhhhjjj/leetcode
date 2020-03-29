# -*- coding: utf-8 -*-
class Solution:
    def maxDistance(self, grid: [[int]]) -> int:
        # 找到一个距离最远的，先把所有的1找出来还是怎么样？一次遍历肯定完不成
        # 其实这种小岛题基本都是广度优先搜索
        # 先找到所有陆地，然后陆地不断扩展，直到无法扩展，最终返回step，可以原地修改也可以用个额外的来记录
        n = len(grid)
        steps = -1
        queue = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        # 将所有陆地加入进去

        if len(queue) == 0 or len(queue) == n ** 2: return steps
        # 其他情况

        while len(queue) > 0:
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                for xi, yj in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if xi >= 0 and xi < n and yj >= 0 and yj < n and grid[xi][yj] == 0:
                        queue.append((xi, yj))
                        grid[xi][yj] = -1
            steps += 1

        return steps
    # 突然发现昨天改了git之后，现在上传的账号没了，在这在option里面把邮箱改回来