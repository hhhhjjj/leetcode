# -*- coding: utf-8 -*-
class Solution:
    def displayTable(self, orders: [[str]]) -> [[str]]:
        # 这题目好无聊，直接哈希表就完事了
        table = {}
        Ftype = set()
        for Name, Num, food in orders:
            if Num in table:
                if food in table[Num]:
                    table[Num][food] += 1
                else:
                    table[Num][food] = 1
            else:
                table[Num] = {food: 1}
            Ftype.add(food)
        Nums = sorted(table.keys(), key=lambda x: int(x))
        Foods = sorted(list(Ftype))
        n = len(Foods)
        Table = [["Table"] + Foods] + [[str(_)] + ["0" for __ in range(n)] for _ in Nums]
        for i in range(1, len(Table)):
            for idx, F in enumerate(Foods):
                if F in table[Table[i][0]]:
                    Table[i][idx + 1] = str(table[Table[i][0]][F])
        return Table