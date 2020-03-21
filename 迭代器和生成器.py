# -*- coding: utf-8 -*-
# 上次差点翻车了，回顾一下
s = 'abc'
it = iter(s)
# 这就是迭代器，每次都是用next
# print(next(it))

# 生成器也是一种迭代器，但是只能迭代一次，因为没把所有值存在内存中，一边循环一边计算
# 比如一个列表贼大，但是我只用前几个数
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        # 从上次的位置继续下去
        yield data[index]

for char in reverse('golf'):
    print(char)





