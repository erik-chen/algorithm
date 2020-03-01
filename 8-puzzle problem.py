from random import *
from time import *

"""
1  2  6   0  1  2
8  4  3 → 3  4  5
7  5  0   6  7  8
"""
# BFS


class Queue(object):

    def __init__(self):
        self._numbers = [0 for x in range(400000)]
        self._head = 0
        self._tail = 0

    @property
    def numbers(self):
        return self._numbers

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def stack_empty(self):
        if self._head == self._tail:
            return True
        else:
            return False

    def enqueue(self, x):
        if self._head - self._tail == 1 or self._head == 0 and self._tail == 400000-1:
            print('error: overflow')
        else:
            self._numbers[self._tail] = x
            if self._tail == 400000-1:
                self._tail = 0
            else:
                self._tail += 1

    def dequeue(self):
        if self.stack_empty():
            print('error: underflow')
        else:
            x = self._numbers[self._head]
            if self._head == 400000-1:
                self._head = 0
            else:
                self._head += 1
        return x

    def __str__(self):
        if self._head <= self._tail:
            queue_str = str(self._numbers[self._head:self._tail])
        else:
            queue_str = str(self._numbers[self._head:400000]+self._numbers[0:self._tail])
        return queue_str


def BFS(start, goal):
    queue = Queue()
    have_traveled = []
    queue.enqueue(start)
    have_traveled.append(start)
    while queue.head != queue.tail:
        order = queue.numbers[queue.head]
        order_change_list = []
        print(len(have_traveled))
        print('queue长度', queue.tail-queue.head)
        _0_position = order.find('0')
        if 0 <= _0_position-3 <= 8:
            order_change_list.append(order[0:_0_position-3] + '0' + order[_0_position-2:_0_position] + order[_0_position-3] + order[_0_position+1:])
        if 0 <= _0_position+3 <= 8:
            order_change_list.append(order[0:_0_position] + order[_0_position+3] + order[_0_position+1 :_0_position+3] + '0' + order[_0_position+4:])
        if 0 <= _0_position-1 <= 8:
            order_change_list.append(order[0:_0_position-1] + '0' + order[_0_position-1] + order[_0_position+1:])
        if 0 <= _0_position+1 <= 8:
            order_change_list.append(order[0:_0_position] + order[_0_position+1] + '0' + order[_0_position+2:])
        for new_order in order_change_list:
            if new_order not in have_traveled:
                queue.enqueue(new_order)
                have_traveled.append(new_order)
                if new_order == goal:
                    print(len(have_traveled))
                    return
        queue.dequeue()


def shuffle_str(s):
    str_list = list(s)
    shuffle(str_list)
    return ''.join(str_list)


def calculate(start):
    a = (start.find('0'))
    start = start[:a]+start[a+1:]
    start = list(start)
    num = 0
    for i in range(len(start)):
        for j in range(i+1, len(start)):
            if start[i] > start[j]:
                num += 1
    return num


if __name__ == '__main__':
    start = '412375608'
    goal = shuffle_str(start)
    print(goal)
    if (calculate(start)-calculate(goal))%2 == 1:
        print('此题无解')
    else:
        BFS(start, goal)



