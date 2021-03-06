# -*- coding: utf-8 -*-
# 现在有100瓶药，只有1瓶是有毒的，老鼠试完药后，需要3天才能才能知道药是否有毒，而现在需要3天知道100瓶中哪1瓶有毒，请问最少需要多少只老鼠
# 这个题目肯定不是一百瓶，这个是转换成二进制来看就可以具体到哪一位了，100小于2的7次方，所以只要7只老鼠就行
#
# 两堆苹果，一堆6个，一堆7个，取法两种，再其中一堆取一个，两堆各取一个，先拿，如何获胜
# 先从一堆中取一个然后跟着对方取一样的就行。反正都会乘以2
#
# 有100个红球，100个篮球，两个桶，怎么把这200个球放到桶中使得随便从桶中取一个球是红球的概率最高
# 这个题目就是一个桶放红球，另外一个桶放其他所有的球，自己算概率0.5 + 99/199*0.5= 0.748
#
# 25匹马5赛道选出最快的三匹
# 5 + 1 + 1就行
#
# 给定两条绳子，每条绳子烧完正好一个小时，并且绳子是不均匀的。问要怎么准确测量 15 分钟
# 点燃第一条的两头，同时点第二条的一头，这时候第一条烧完时候过了三十分钟，然后再点第二条的两头，烧完正好15分钟
#
# 有 9 个球，其中 8 个球质量相同，有 1 个球比较重。要求用 2 次天平，找出比较重的那个球。
# 将这些球分成三组，选两组称，然后直到哪一组重，然后那一组三个再分三组重复步骤就行
#
# 有 20 瓶药丸，其中 19 瓶药丸质量相同为 1 克，剩下一瓶药丸质量为 1.1 克。瓶子中有无数个药丸。要求用一次天平找出药丸质量 1.1 克的药瓶。
# 可以从药丸的数量上来制造差异：从第 i 瓶药丸中取出 i 个药丸，然后一起称重。可以知道，如果第 i 瓶药丸重 1.1 克/粒，那么称重结果就会比正常情况下重 0.1 * i 克。
# 这个其实就是多出来多少，那么就对应到了具体的位置
#
# 有两个杯子，容量分别为 5 升和 3 升，水的供应不断。问怎么用这两个杯子得到 4 升的水。
# 从 5 做减法得到 4，即最后一个运算应该为 5 - 1 = 4，此时问题转换为得到 1 升的水；1 升的水可以由 3 做减法得到，3 - 2 = 1，此时问题转换为得到 2 升的水；5 - 3 = 2
#
# 一栋楼有 100 层，在第 N 层或者更高扔鸡蛋会破，而第 N 层往下则不会。给 2 个鸡蛋，求 N，要求最差的情况下扔鸡蛋的次数最少
# 这个其实就是动态规划。为了使最坏情况下 E1 和 E2 总共遍历的次数比较少，那么后面的区间大小要比前面的区间更小。具体来说，E1 每多遍历一次，E2 要少遍历一次，才使得 N 无论在哪个区间，总共遍历的次数一样
# 设第一个区间大小为 X，那么第二个区间的大小为 X-1，以此类推。那么 X + (X-1) + (X-2) + … + 1 = 100，得到 X (X + 1) / 2 = 100 ，即 X = 14

# 有100个球，两个人顺序抽球，任意抽1-4个球，问是你先抽还是第二次抽能保证使你抽到最后一个球？
#
# 答案：第二个抽取的可以拿到最后一个球
# 区间划分，抽取求的范围是1-4.则两个人抽取的范围是2-8.但是8个球不能保证，可以保证的范围是2-5个球，
# 因此，将100个球进行缩小范围是5个球，则要拿到第5个球，则需要拿到第0个球，即就是对方先抽取。