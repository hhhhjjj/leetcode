# -*- coding: utf-8 -*-
# 数组拿掉一个数字
ls_old = [1,2,3,3]
ls = [1,2,3]

# 第一种方法用哈希表记录新的数组中所有数字出现的次数
# 然后再去旧的数组里面遍历一遍，
# 次数不对的就是被拿掉的
# 这样子的话遍历了两次，
# 时间复杂度为n，空间复杂度为n
# 用什么排序之后再遍历也可以


def solution(ls_old, ls):
    my_dict = {}
    for num in ls:
        if my_dict.get(num) is None:
            my_dict[num] = 1
        else:
            my_dict[num] += 1
    res = []
    for num in ls_old:
        if my_dict.get(num) is None \
                or my_dict[num] == 0:
            res.append(num)
        else:
            my_dict[num] -= 1
    return res

# 第二种方法就是用异或，
# 如果a、b两个值不相同，则异或结果为1。
# 如果a、b两个值相同，异或结果为0
# 速度快，
# 而且不需要额外的空间复杂度


def solution2(ls_old,ls):
    res = int()
    for num in ls_old:
        res ^= num
    for num in ls:
        res ^= num
    return res

# 然后讨论拿掉两个数字
ls_old = [1,2,3,4]
ls = [1,2]

# 之前哈希表的方法肯定是可以的
# 在这追求只遍历一遍
# 在这把原数组分成两个子数组，
# 每个子数组中包含一个只出现一次的数字
# 而其他数字都出现两次，这就变成上面的解决方法了
# 从头到尾依次异或数组中的每一个数字，那么最终得到的结果就是两个只出现一次的数字的异或结果
# 结果数字的二进制表示中至少就有一位为1。
# 我们在结果数字中找到第一个为1的位的位置，记为第N位。
# 现在我们以第N位是不是1为标准把原数组中的数字分成两个子数组，
# 第一个子数组中每个数字的第N位都为1，而第二个子数组的每个数字的第N位都为0

from functools import reduce
# 还有个方法就是直接方程组出来
# x + y = sum(ls_old) - sum(ls)
# x * y = reduce(lambda x, y: x * y, ls_old) / reduce(lambda x, y: x * y, ls)
# 然后就可以算出来x和y的结果了

x = (((sum(ls_old) - sum(ls))**2) / 4 -
     reduce(lambda x, y: x * y, ls_old) /
     reduce(lambda x, y: x * y, ls))**0.5\
    + sum(ls_old) - sum(ls)

y = sum(ls_old) - sum(ls) - x

