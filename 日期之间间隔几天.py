# -*- coding: utf-8 -*-
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # 这题目要是自己做折腾半天，直接调用datetime库就行
        import datetime
        date1 = datetime.datetime.strptime(date1,"%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2,"%Y-%m-%d")
        return abs((date1 - date2).days)

print(Solution().daysBetweenDates(date1 = "2019-06-29", date2 = "2019-06-30"))