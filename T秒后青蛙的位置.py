# -*- coding: utf-8 -*-
class Solution:
    def frogPosition(self, n: int, edges: [[int]], t: int, target: int) -> float:
        # 这个是无向图
        length0 = len(edges)
        if length0 == 0:
            return 0
        if target == 1:
            return 1
        word_dict = {}
        index_dict = {}
        flag = 0
        for i in range(length0):
            if flag != 0 and edges[i][0] != flag:
                res = float(1 / len(word_dict[flag]))
                while flag != 1:
                    flag = index_dict[flag]
                    res *= float(1 / len(word_dict[flag]))
                return res
            index_dict[edges[i][1]] = edges[i][0]
            if word_dict.get(edges[i][0]):
                word_dict[edges[i][0]].append(edges[i][1])
            else:
                word_dict[edges[i][0]] = [edges[i][1]]
            if edges[i][1] == target:
                flag = edges[i][0]
        res = float(1 / len(word_dict[flag]))
        print(word_dict)
        print(index_dict)
        while flag != 1:
            flag = index_dict[flag]
            res *= float(1 / len(word_dict[flag]))
        return res


print(Solution().frogPosition(3, [[2,1],[3,2]] ,1 , 2))