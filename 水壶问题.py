# -*- coding: utf-8 -*-
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        import math
        # 想了半天其实不过是个数学问题
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0
# 这个gcd是返回最大公约数



print(Solution().canMeasureWater(x = 2, y = 6, z = 5))



