# -*- coding: utf-8 -*-
class Solution:
    def isPossible(self, target: [int]) -> bool:
        # 每一次是加length - 1
        length = len(target)
        target.sort()
        cur = 0
        the_num = 1
        add_num = 1
        while True:
            if the_num == target[cur]:
                if cur == length - 1:
                    return True
                else:
                    if the_num == 1:
                        cur += 1
                    else:
                        cur += 1
                        the_num += the_num

            elif the_num > target[cur]:
                return False
            else:
                the_num += (length - 1) * add_num
            print(the_num)


print(Solution().isPossible([73,1,25,7,37,1,1]))