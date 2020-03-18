# -*- coding: utf-8 -*-
class Solution:
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
        n = len(gas)

        total_tank, curr_tank = 0, 0
        starting_station = 0
        # 这里来记录开始的位置
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # 在这就重新开始，但是总的油量不重置
                curr_tank = 0

        return starting_station if total_tank >= 0 else -1




print(Solution().canCompleteCircuit(gas  = [1,2,3,4,5], cost = [3,4,5,1,2]))

