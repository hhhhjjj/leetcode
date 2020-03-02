# -*- coding: utf-8 -*-
class Solution:
    def rankTeams(self, votes: [str]) -> str:
        # 直接用权重的还是不靠谱，有bug
        import collections
        n = len(votes[0])
        # 初始化哈希映射
        # 这个defaultdict就是在如果没有这个key但是又被查询的时候设置默认值
        # 这里的默认值就是各个阶段排名的次数
        ranking = collections.defaultdict(lambda: [0] * n)
        # 遍历统计
        for vote in votes:
            for i, vid in enumerate(vote):
                ranking[vid][i] += 1

        # 取出所有的键值对
        result = list(ranking.items())
        # 排序
        result.sort(key=lambda x: (x[1], -ord(x[0])), reverse=True)
        return "".join([vid for vid, rank in result])

print(Solution().rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"]))



