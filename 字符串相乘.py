# -*- coding: utf-8 -*-
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
#         这个不让直接转
        length1 = len(num1)
        length2 = len(num2)
        if length2 == 0 or length1 == 0:
            return str(None)
        if num2 == "0" or num1 == "0":
            return "0"
        # 这个就是小学的乘法，或者直接全转完再相乘也行
#         这题好无聊




