#!/usr/bin/python
# -*- coding: utf-8 -*-
__version__ = '0.0.1'
__author__ = 'fanding'
import json


class LinkNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SingleLinkList():
    def __init__(self):
        self.head = LinkNode()
        self.size = 0

    # 增
    def insertFisrt(self, value):  # 向头部插入
        linkNode = LinkNode()
        linkNode.data = value
        linkNode.next = self.head.next
        self.head.next = linkNode
        self.size += 1

    def insertLast(self, value):  # 向尾部插入
        tempNode = self.head
        linkNode = LinkNode()
        linkNode.data = value
        while tempNode.next:
            tempNode = tempNode.next
        tempNode.next = linkNode
        self.size += 1

    def insert(self, index, value):  # 向指定位置插入元素
        '''
        index: 是第几个的意思，不是下标的意思
        注意：空链表无法使用该方法，insert(index=1, value=0)会报错
        '''
        if index <= 0 or index > (self.size):
            raise ValueError('index is out of range!')
        linkNode = LinkNode(data=value)
        tempNode = self.find(index=index - 1)
        linkNode.next = tempNode.next
        tempNode.next = linkNode
        self.size += 1

    # 删除
    def delFirst(self):  # 删除第一个元素
        if self.size == 0:
            raise ValueError('delError!')
        tempNode = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return tempNode

    def delLast(self):  # 删除最后一个元素
        if self.size == 0:
            raise ValueError('delError!')
        tempNode = self.head
        while tempNode.next.next:  # 寻找最后一位的前一位
            tempNode = tempNode.next
        tempNode.next = None
        self.size -= 1

    def delete(self, index):  # 删除指定位置元素
        '''
        index: 表示第几位而不是数组中的下标，从非头结点计算（头结点不算第一个）
        '''
        if index <= 0 or index > self.size:
            raise ValueError('index is out of range!')
        tempNode = self.find(index=index - 1)
        if tempNode.next.next:
            tempNode.next = tempNode.next.next
        else:
            tempNode.next = None
        self.size -= 1

    # 修改
    def alterValue(self, index, value):
        if index <= 0 or index > self.size:
            raise ValueError('index is out of range!')
        tempNode = self.find(index=index)
        tempNode.data = value

    # 查找
    def find(self, index):  # 查找第index位的元素
        if index < 0 or index > self.size:
            raise ValueError('index is out of range!')
        if index == 0:
            return self.head
        tempNode = self.head
        count = 0
        while count < index:
            tempNode = tempNode.next
            count += 1
        return tempNode

    def index(self, value):  # 查找第一个值匹配元素的位置，头结点不算
        if self.size == 0:
            return -1
        tempNode = self.head.next
        count = 1
        while tempNode:
            if tempNode.data == value:
                return count
            tempNode = tempNode.next
            count += 1
        return -1

    def changeToCycle(self):
        tempNode = self.find(self.size)
        tempNode.next = self.head

    def __str__(self):
        data = {
            'data': [],
            'size': self.size
        }
        tempNode = self.head.next
        if not tempNode:
            return json.dumps(data)
        while (tempNode):
            data['data'].append(tempNode.data)
            tempNode = tempNode.next
        return json.dumps(data)


if __name__ == '__main__':
    singleLinkList = SingleLinkList()
    singleLinkList.insertFisrt(value=1)
    singleLinkList.insertFisrt(value=2)
    singleLinkList.insertFisrt(value=3)
    singleLinkList.insertFisrt(value=4)
    print(singleLinkList)

    singleLinkList.insertLast(value=1)
    print(singleLinkList)

    singleLinkList.insert(index=1, value=9)
    print(singleLinkList)

    singleLinkList.delFirst()
    print(singleLinkList)
    singleLinkList.delLast()
    print(singleLinkList)

    a = singleLinkList.find(index=4)
    print(a.data)

    print(singleLinkList.index(3))

    singleLinkList.delete(index=2)
    print(singleLinkList)
