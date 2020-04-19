# -*- coding: utf-8 -*-
class Solution:
    def minJump(self, jump: [int]) -> int:
        # 之前的题目是问能不能跳出去，现在这个就要求最小的跳跃次数
        # 还是bfs，然后记录状态
        visit = [0 for _ in range(len(jump))]
        # 队列，记录一个元组：（当前位置，当前jump次数）
        # 初始状态为（0，0）
        q = [(0, 0)]
        visit[0] = 1
        # 该参数记录已访问过的最大index，该位置左边的弹簧均已被遍历
        # 对于i<=max_left_idx, visit[i]==1。
        max_left_idx = 0
        # BFS遍历
        while q:
            cur_idx, count = q.pop(0)
            # 情况1: 向右跳
            right_idx = cur_idx + jump[cur_idx]
            # 小球弹出机器只可能发生在向右跳的情况，小球弹出时返回答案
            if right_idx >= len(jump):
                return count + 1
            else:
                if not visit[right_idx]:
                    q.append((right_idx, count + 1))
                    visit[right_idx] = 1
            # 情况2: 向左跳
            # max_left_idx左边的弹簧已经遍历过，不需要再访问，直接从max_left_idx+1开始遍历至cur_idx
            # 如果不设置该参数，需要从0遍历置cur_idx，造成TLE错误
            for i in range(max_left_idx + 1, cur_idx):
                if not visit[i]:
                    q.append((i, count + 1))
                    visit[i] = 1
            # 更新max_left_idx的值，即当前cur_idx左边的弹簧已经遍历过
            max_left_idx = cur_idx


