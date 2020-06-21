# -*- coding: utf-8 -*-
str_ls = []
# 这题目倒是不难
# 牛客这傻逼网站真的是输入输出麻烦

while True:
    try:
        # 主要还都是要用这个格式
        # 这个先是输入的次数
        a= int(input())
        for i in range(a):
            # 这里才得到输入的字符串，这个居然是分次数输入进来。。。
            s=input()
            while len(s)>8:
                print(s[:8])
                s=s[8:]
            print(s.ljust(8,"0"))
    #         这个就是左对齐，0是填充的字符，默认是空格
    except:
        break