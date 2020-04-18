# -*- coding: utf-8 -*-
class Solution:
    def numWays(self, n: int, relation: [[int]], k: int) -> int:
        self.res = 0
        if not relation:
            return self.res
        self.rel_dict = {}
        for rel in relation:
            if self.rel_dict.get(rel[0]):
                self.rel_dict[rel[0]].append(rel[1])
            else:
                self.rel_dict[rel[0]] = [rel[1]]

        def helper(rel_in, k_in):
            if k_in < 0:
                pass
            elif k_in == 0 and rel_in == n - 1:
                self.res += 1
            else:
                if self.rel_dict.get(rel_in):
                    for rel0 in self.rel_dict[rel_in]:
                        helper(rel0, k_in - 1)

        helper(0, k)
        return self.res





print(Solution().numWays(n = 3, relation = [[0,2],[2,1]], k = 2))

