"""
    题目：n个人依次前来应聘，如果下个人较为出色，则雇佣新人，
    请问聘用1、2、……、n次的概率是多少？(《算法导论》P65)
    作者：陈志豪
    日期：2019、08、23
"""
from datetime import datetime
from math import *
from time import time


def method_1(n):
    def sub(n, original_n):
        c = [0] * original_n
        if n == 1:
            c[0] = 1
        if n > 1:
            c[1] += 1 / (n - 1)
            for i in range(2, n):
                for index, value in enumerate(sub(i, original_n)[0:i]):
                    c[index + 1] += 1 / (n - 1) * value
        return c

    original_n = n
    total = [0] * original_n
    for i in range(0, original_n):
        # print('sub_starts_with_{}='.format(10-i), sub(i+1, original_n))
        for j in range(1, original_n+1):
            total[i] += sub(j, original_n)[i]
    for i in range(0, original_n):
        total[i] /= original_n
    print('递归方法结果为', total)
    print('归纳方法概率总和', fsum(total))


def method_2(n):
    a = [0] * n
    a[1] = [1]
    b = [0] * n
    b[0] += 1/n
    for k in range(2, n):
        a[k] = [0] * k
        a[k][0] = 1 / k
        for i in range(1, k):
            for j in range(len(a[i])):
                a[k][j+1] += 1/k * a[i][j]
        # print(a[k])
    for k in range(1, n):
        for m in range(len(a[k])):
            b[m+1] += a[k][m]/n
    print('归纳方法结果为', b)
    print('归纳方法概率总和', fsum(b))


if __name__ == '__main__':
    n = 5
    time_0 = datetime.now()
    kk1 = time()
    method_1(n)
    time_1 = datetime.now()
    kk2 = time()
    method_2(n)
    time_2 = datetime.now()
    kk3 = time()

    print('递归方法用时', time_1 - time_0)
    print('递归方法用时', kk2 - kk1)
    print('归纳方法用时', time_2 - time_1)
    print('递归方法用时', kk3 - kk2)