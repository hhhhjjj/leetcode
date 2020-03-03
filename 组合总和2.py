# -*- coding: utf-8 -*-
class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        if candidates == [] or target is None:
            return [[]]
        res = []
        candidates.sort()
        # candidates = list(set(candidates))
        # 不要去重，第一个还要用后面的
        def helper(path, now_sum, candidates_in):
            for i in range(len(candidates_in)):
                if i > 0 and candidates_in[i] == candidates_in[i - 1]:
                    pass
                else:
                    if candidates_in[i] + now_sum == target:
                        res.append(path[:] + [candidates_in[i]])
                    elif candidates_in[i] + now_sum < target:
                        path.append(candidates_in[i])
                        now_sum += candidates_in[i]
                        if i != len(candidates_in) - 1:
                            # 结果都出来了，但是要去重，所以这里只往后接后面部分的
                            helper(path, now_sum, candidates_in[i + 1:])
                        path.pop()
                        now_sum -= candidates_in[i]
        helper([], 0, candidates)
        return res

print(Solution().combinationSum2(candidates = [2,5,2,1,2], target = 5))





