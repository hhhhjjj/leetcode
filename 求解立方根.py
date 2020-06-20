# -*- coding: utf-8 -*-
# data=list(map(int,input().split()))
# 输入多个字符才用这个，输入一个直接input就行
# print(data)
# 我靠，我发现一个都做不出来
data = 9
# 我觉得这个就是一点点试出来
# 其实发现不用math库也行
# data = input('')
print('%.1f' % (float(data)**(1/3.0)))
# 想要弄的话就二分查找，也不要去一点点试
# 输入的数，和最小的之间，不停的二分查找，精度提高就行

