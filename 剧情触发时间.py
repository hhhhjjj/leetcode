# -*- coding: utf-8 -*-
class Solution:
    def getTriggerTime(self, increase: [[int]], requirements: [[int]]) -> [int]:
        increase = [[0, 0, 0]] + increase
        length = len(requirements)
        length_i = len(increase)
        res = [-1] * length
        # 这个题感觉就根据c来构建个索引把
        c_dict = {}
        ruler = []
        for i in range(length):
            if c_dict.get(requirements[i][0]):
                c_dict[requirements[i][0]].append(i)
            else:
                c_dict[requirements[i][0]] = [i]
                ruler.append(requirements[i][0])
        ruler.sort()
        C = 0
        R = 0
        H = 0
        for inc in range(length_i):
            C += increase[inc][0]
            R += increase[inc][1]
            H += increase[inc][2]
            for r in ruler:
                if r <= C:
                    del_list= []
                    for i in c_dict[r]:
                        if requirements[i][0] <= C and requirements[i][1] <= R and requirements[i][2] <= H:
                            res[i] = inc
                            del_list.append(i)
                    for i in del_list:
                        c_dict[r].remove(i)
        return res
# 还是超时了

print(Solution().getTriggerTime(increase = [[0,4,5],[4,8,8],[8,6,1],[10,10,0]],requirements = [[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]]))