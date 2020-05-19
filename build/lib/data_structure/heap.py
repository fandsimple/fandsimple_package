#!/usr/bin/python
# -*- coding: utf-8 -*-
import json


class Heap():
    def __init__(self, capacity=100):
        self.size = 0  # 当前存储元素个数
        self.capacity = capacity  # 最大容纳元素个数
        self.dataList = [None] * self.capacity  # 数据域

    def insert(self, value):  # 插入操作
        '''
        时间复杂度：O(logn)
        空间复杂度：O(1)
        '''
        if self.size >= self.capacity:
            raise ValueError('heap is full!!')
        self.size += 1
        self.dataList[self.size] = value  # 数据插入，自下而上进行heapify
        i = self.size
        while (i // 2) > 0 and self.dataList[i] > self.dataList[i // 2]:
            self.dataList[i], self.dataList[i // 2] = self.dataList[i // 2], self.dataList[i]
            i = i // 2

    def removeMax(self):  # 删除元素
        '''
        时间复杂度：O(logn)
        空间复杂度：O(1)
        '''
        if self.size <= 0:
            raise ValueError('heap is empty!!')
        self.dataList[1], self.dataList[self.size] = self.dataList[self.size], self.dataList[1]
        self.size -= 1
        self.heapify(self.dataList, self.size, 1)

    def heapify(self, dataList, n, i):  # 堆化函数
        if len(dataList) == 0:
            return
        max = i
        while True:
            if i * 2 <= n and dataList[i] < dataList[i * 2]:
                max = i * 2
            if (i * 2 + 1) <= n and dataList[max] < dataList[i * 2 + 1]:
                max = i * 2 + 1
            if max == i:
                break
            dataList[i], dataList[max] = dataList[max], dataList[i]
            i = max

    def __str__(self):
        data = {
            'size': self.size,
            'capacity': self.capacity,
            'dataList': self.dataList[1:self.size+1]
        }
        return json.dumps(data)


if __name__ == '__main__':
    myheap = Heap()
    myheap.insert(1)
    myheap.insert(2)
    myheap.insert(3)
    myheap.insert(2)
    myheap.insert(5)
    print(myheap)
    myheap.removeMax()
    print(myheap)
