"""
    题目：《算法导论》P67，题目5.1-3
    作者：陈志豪
    日期：2019、08、15
"""
from random import *


# 构建一个以概率p输出的随机结果函数, 0<p<1
def random_p(p):
    if uniform(0, 1) < p:
        result = 1
    else:
        result = 0
    return result


# 以random_p(p)为子程序，构建函数
def main(p):
    while True:
        result1 = random_p(p)
        result2 = random_p(p)
        if result1 == 0 and result2 == 1:
            result = 1
        elif result1 == 1 and result2 == 0:
            result = 0
        else:
            result = main(p)
        return result

# 1/p(1-p)


i = 0
for j in range(100000):
    if main(0.4) == 1:
        i += 1
print(i)



