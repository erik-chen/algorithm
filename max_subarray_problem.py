"""
    题目：在给定数组中找其子数组，使得子数组的元素之和最大(《算法导论》P38)
    作者：陈志豪
    日期：2019、08、13
"""
from random import *
from datetime import datetime
from math import *


# A为原题目数组，长度16
A = [13, -3, -25, 20, -3, -16, -23, 18,
     20, -7, 12, -5, -22, 15, -4, 7]
# B为一般性数组，长度任意
B = [randint(-6000, 10000) for x in range(100)]


# 暴力求解方法
def method_1(A):
    max = -999
    i_max = j_max = -1
    for i in range(len(A)):  # len(A) = 16
        for j in range(i+1, len(A)+1):  # len(A) = 16
            sum = fsum(A[i:j])
            if sum > max:
                max = sum
                i_max, j_max = i, j
    while A[i_max] == 0:
        i_max += 1
    return A[i_max: j_max]


# 自己想出来的算法，似乎很朴素
def method_2(A):
    max = float('-inf')
    i_max = j_max = -1
    i, j = 0, 1
    sum = 0
    for j in range(1, len(A)+1):  # len(A) = 16
        sum += A[j - 1]
        if A[j-1] >= 0:
            if sum > max:
                max = sum
                i_max, j_max = i, j
        elif A[j-1] < 0:
            if sum < 0:
                i = j
                sum = 0
    while A[i_max] == 0:
        i_max += 1
    return sum(A[i_max: j_max])


# 分治方法
def method_3(A):
    if len(A) >= 2:
        p = len(A)//2
        left_max_subarray = method_3(A[0:p])
        right_max_subarray = method_3(A[p:2*p])
        max_left = max_right = -999
        sum_left = sum_right = 0
        i_max = j_max = -1
        for i in range(p-1, -1, -1):
            sum_left += A[i]
            if sum_left > max_left:
                max_left = sum_left
                i_max = i
        for j in range(p+1, 2*p+1, 1):
            sum_right += A[j-1]
            if sum_right > max_right:
                max_right = sum_right
                j_max = j
        mid_max_subarray = A[i_max: j_max]
        if fsum(left_max_subarray) > fsum(right_max_subarray) \
                and fsum(left_max_subarray) > fsum(mid_max_subarray):
            max_subarray = left_max_subarray
        else:
            if fsum(right_max_subarray) > fsum(mid_max_subarray):
                max_subarray = right_max_subarray
            else:
                max_subarray = mid_max_subarray
        return max_subarray
    if len(A) == 1:
        return A


def main():
    time_0 = datetime.now()
    answer_1 = method_1(B)
    time_1 = datetime.now()
    answer_2 = method_2(B)
    time_2 = datetime.now()
    answer_3 = method_3(B)
    time_3 = datetime.now()

    print('暴力解法结果：', answer_1)
    print('自创解法结果：', answer_2)
    print('分治解法结果：', answer_3)
    print('暴力解法用时：', time_1 - time_0)
    print('自创解法用时：', time_2 - time_1)
    print('分治解法用时：', time_3 - time_2)


if __name__ == '__main__':
    main()


