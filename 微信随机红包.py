# -*- coding: utf-8 -*-
import random
def hb_generator(hongbao_num, money_sum):
        # 其实这个就是把总金额区间等分，但是每个区间的期望应该是相同的
        hongbao_remain = hongbao_num
        for i in range(hongbao_num -1):
            min = 0.01
            max = money_sum/hongbao_remain*2
            money = round(random.uniform(0, max), 2)
            hongbao_money = money if money > min else min
            hongbao_remain -= 1
            money_sum -= hongbao_money
            yield hongbao_money
        yield round(money_sum, 2)