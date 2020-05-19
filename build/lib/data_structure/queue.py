#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
队列的类型：
    实现底层结构：
        顺序队列
        链式队列

    功能划分：
        一般队列
        阻塞队列：
            插入、删除带有阻塞性质
        并发队列（线程安全队列）：
            链式队列：
                在添加或者删除操作上加锁实现
            顺序队列：
                CAS原子操作进行

队列的应用：
    情景：1、对有限资源进行访问。 2、满足公平性，先到的先分配。
    1、线程池、数据库连接池
    2、还有一些消息队列等等
'''
from data_structure import SingleLinkList

from data_structure import LinkNode
import json


class Queue():  # 链式队列
    def __init__(self):
        self.linkList = SingleLinkList()
        self.size = self.linkList.size
        self.head = self.linkList.head
        self.tail = self.linkList.head

    def enqueue(self, value):  # 入队
        linkNode = LinkNode(data=value)
        self.tail.next = linkNode
        self.tail = linkNode
        self.size += 1

    def dequeue(self):  # 出队
        if self.size == 0:
            raise ValueError('linkList is empty!')
        tempNode = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return tempNode

    def __str__(self):
        data = {
            'data': [],
            'size': self.size
        }
        tempNode = self.linkList.head.next
        if self.size == 0:
            return json.dumps(data)
        while (tempNode):
            data['data'].append(tempNode.data)
            tempNode = tempNode.next
        return json.dumps(data)


class OrderQueue():
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0
        self.head = self.tail = 0

    # 队空：self.head == self.tail     队满：（self.tail + 1）% self.capacity == self.head
    # 注意：队列tail位置不存储元素
    def enqueue(self, value):
        if ((self.tail + 1) % self.capacity) == self.head:
            raise ValueError('queue is full!')
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.head == self.tail:
            raise ValueError('queue is empty!')
        tempNode = self.data[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return tempNode

    def __str__(self):
        data = {
            'data': [],
            'size': self.size
        }
        pre = self.head
        cur = self.tail
        while pre != cur:
            data['data'].append(self.data[pre])
            pre = (pre + 1) % self.capacity
        return json.dumps(data)



if __name__ == '__main__':
    # queue = Queue()
    # print(queue)
    # queue.enqueue(1)
    # queue.enqueue(2)
    # queue.enqueue(3)
    # print(queue)
    #
    # print(queue.dequeue().data)
    # print(queue)
    # print(queue.tail.data)

    orderqueue = OrderQueue()
    print(orderqueue)
    orderqueue.enqueue(1)
    print(orderqueue)

    orderqueue.enqueue(2)
    orderqueue.enqueue(3)
    print(orderqueue.dequeue())
    orderqueue.enqueue(4)
    orderqueue.enqueue(5)
    orderqueue.enqueue(6)
    orderqueue.enqueue(7)
    orderqueue.enqueue(7)
    print(orderqueue.dequeue())
    # print(orderqueue.dequeue())
    # print(orderqueue.dequeue())
    # print(orderqueue.dequeue())
    # print(orderqueue.dequeue())
    # print(orderqueue.dequeue())
    print(orderqueue)

