# -*- coding: utf-8 -*-
class Solution:
    def rankTeams(self, votes: [str]) -> str:
        length_vote = len(votes)
        if length_vote == 0:
            return ""
        if length_vote == 1:
            return votes[0]
        length_v = len(votes[0])
        # 想直接做个权重，这个长度最大1000，也就是说上一级的权重只要为1001就不用担心后面的能追上来
        word_dict = {}
        for i in votes:
            for j in range(length_v):
                if word_dict.get(i[j]):
                    word_dict[i[j]] += 1001*(length_v - j)
                else:
                    word_dict[i[j]] = 1001 * (length_v - j)

        d_order = sorted(word_dict.items(), key = lambda x:x[1] + [90 - ord(x[0])],reverse= True)

        return ""

print(Solution().rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"]))



