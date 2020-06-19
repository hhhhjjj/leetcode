# -*- coding: utf-8 -*-
# 牛客这东西输入输出也不告诉我。。。，反正就照着leetcode的来吧
# 没想到第一道题就难倒我了
# 有两种方法，一个是更相减损，一个是辗转相除
# 最小公倍数=两数相除乘以最大公约数
# 更相减损就是两个数中较大的减较小的，然后在减数，被减数，差之间取两个较小的继续相减，直到减数和被减数相等，这时候就是最大公约数了
# 我都不知道这个是怎么验证出来这个结论的。。。
def solution(A, B):
    def method(min_A_in, min_B_in):
        if min_A_in == min_B_in:
            return min_A_in
        elif min_A_in > min_B_in:
            differ = min_A_in - min_B_in
            return method(min_B_in, differ)
        else:
            differ = min_B_in - min_A_in
            return method(min_A_in, differ)

    min_A = A
    min_B = B
    return int(A * B / method(min_A, min_B))

print(solution(328,7751))
# 这个牛客网是真的傻逼，居然用的 input才嫩出来
import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


while True:
    n = sys.stdin.readline().strip()
    # 还需要这么费劲在这取数
    if n:
        n = n.split(' ')
        if len(n) > 1:
            a = int(n[0])
            b = int(n[1])
            print(a * b // gcd(a, b))
    else:
        break

