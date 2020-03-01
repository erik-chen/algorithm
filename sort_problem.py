from random import *
from copy import *
from datetime import *
import sys


sys.setrecursionlimit(15000)  # set the maximum depth as 15000


def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key


def merge_sort(a):
    if len(a) >= 2:
        left, right, a = merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:]), []
        while left or right:
            p = left if left and (not right or left[0] <= right[0]) else right; a.append(p[0]); del p[0]
    return a


def heap_sort(a):
    def max_heapify(a, i=0, n=len(a)):
        left = 2*i+1
        right = 2*i+2
        largest = i
        if left < n and a[left] > a[i]:
            largest = left
        if right < n and a[right] > a[largest]:
            largest = right
        if largest != i:
            a[largest], a[i] = a[i], a[largest]
            max_heapify(a, largest, n)

    def build_max_heap(a):
        for i in range(len(a)//2-1, -1, -1):
            max_heapify(a, i)

    build_max_heap(a)
    for i in range(len(a)-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        max_heapify(a, 0, i)


def quick_sort(a):
    def quick_sort_parameter(a, start=1, end=len(a)):
        if start < end:
            x = a[end-1]
            j = start-1
            for i in range(start-1, end-1):
                if a[i] < x:
                    a[j], a[i] = a[i], a[j]
                    j += 1
            a[j], a[end-1] = a[end-1], a[j]
            quick_sort_parameter(a, start, j)
            quick_sort_parameter(a, j+2, end)

    quick_sort_parameter(a)


def func_sort(a):
    a.sort()


if __name__ == '__main__':
    random_list = [randint(1, 10000) for x in range(10000)]
    a = deepcopy(random_list)
    b = deepcopy(random_list)
    c = deepcopy(random_list)
    d = deepcopy(random_list)
    e = deepcopy(random_list)
    print(random_list)
    time0 = datetime.now()
    insertion_sort(a)
    time1 = datetime.now()
    merge_sort(b)
    time2 = datetime.now()
    heap_sort(c)
    time3 = datetime.now()
    quick_sort(d)
    time4 = datetime.now()
    func_sort(e)
    time5 = datetime.now()
    print(a)
    print(merge_sort(b))
    print(c)
    print(d)
    print(e)
    print('插入排序用时：', time1 - time0)
    print('合并排序用时：', time2 - time1)
    print('堆排序用时：', time3 - time2)
    print('快速排序用时：', time4 - time3)
    print('排序函数用时：', time5 - time4)


