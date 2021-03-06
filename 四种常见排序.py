# -*- coding: utf-8 -*-
# 稳定性就是指两个相等的数应该排序之后前后位置不变
ls = [1,2,5,4]
length = 4
# 冒泡：稳定
for i in range(length - 1):
    for j in range(length - i - 1):
        if ls[j] > ls[j + 1]:
            ls[j], ls[j + 1] = ls[j + 1], ls[j]
# 选择排序，第一轮所有比找最小的放第一个，不稳定，会出现前一个被调到后面去
for i in range(length - 1):
    min_index = i
    for j in range(i + 1, length):
        if ls[j] < ls[min_index]:
            min_index = j
    ls[min_index], ls[i] = ls[i], ls[min_index]
# 插入排序，打牌一样排序，但是还会插入已经排序的里面，稳定
for i in range(1, length):
    for j in range(i, 0, -1):
        if ls[j] < ls[j - 1]:
            ls[j], ls[j - 1] = ls[j - 1], ls[j]
# 快速排序，二分找基准
# 也不稳定
def quicksort(ls_in):
    if len(ls_in) < 2:
        return ls_in
    mid = ls_in[len(ls)//2]
    left, right = [], []
    ls_in.remove(mid)
    for i in ls_in:
        if i >= mid:
            right.append(i)
        else:
            left.append(i)
    return quicksort(left) + [mid] + quicksort(right)
