# -*- coding: utf-8 -*-
class Solution(object):
    def frogPosition(self, n, edges, t, target):
        if target == 1:
            return 1 if n == 1 else 0
        # 这个人和我一样也是用字典来
        # 这个是创建一个新的字典，键就是这个range，值的话在这是none
        dic = dict().fromkeys(range(1,n+1))
        # print(dic)
        for key in dic.keys(): dic[key] = [[],0,1]
        for edge in edges:
            if edge[0]<edge[1]:
                dic[edge[0]][0].append(edge[1])
            else:
                dic[edge[1]][0].append(edge[0])
        queue,level = [], 0
        queue.append(1)
        while queue:
            nextL,level = [], level + 1
            for node in queue:
                for son in dic[node][0]:
                    nextL.append(son)
                    dic[son][1], dic[son][2] = level, dic[node][2] / len(dic[node][0])
                    if son == target:
                        return dic[son][2] if t == dic[son][1] or (t > dic[son][1] and len(dic[son][0])==0) else 0
            queue = nextL


print(Solution().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 20, 6))