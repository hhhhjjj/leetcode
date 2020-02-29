# -*- coding: utf-8 -*-
class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        if strs == []:
            return [[]]
        # 这个不考虑答案输出顺序，拿个字典来就是了
        # 想了半天，一堆多余的步骤就是在浪费时间
        dic = {}
        res = []
        for i in strs:
            # print(str(sorted(i)))
            # 这样子来设置键
            dic.setdefault(str(sorted(i)), []).append(i)
#             setdefault就是查找键，存在就插入，不存在就设置个[]
#         print(dic)
        for value in dic.values():
            res.append(value)
        return res


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

