#!/usr/bin/python
# -*- coding: utf-8 -*-
from data_structure import SingleLinkList


def reverse(singleLinkList):  # 单链表反转
    if not singleLinkList or not singleLinkList.head.next:
        return singleLinkList
    current = singleLinkList.head.next
    preNode = None
    while current:
        tem = current.next  # 作为哨兵，记录current的下一个位置
        current.next = preNode
        preNode = current
        current = tem
    singleLinkList.head.next = preNode


def isCycleLinkList(singleLinkList):  # 检测链表中是否有环
    if not singleLinkList or not singleLinkList.head.next:
        return False
    slow = fast = singleLinkList.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def sortLinkListMerage(linkListOne, linkListTwo):  # 合并两个有序的链表
    if not linkListOne or not linkListOne.head.next:
        return linkListTwo
    if not linkListTwo or not linkListTwo.head.next:
        return linkListOne
    linkListRes = SingleLinkList()
    tempNode = linkListRes.head
    tempNodeOne = linkListOne.head.next
    tempNodeTwo = linkListTwo.head.next
    while tempNodeOne and tempNodeTwo:
        if tempNodeOne.data > tempNodeTwo.data:
            tempNode.next = tempNodeTwo
            tempNodeTwo = tempNodeTwo.next
        else:
            tempNode.next = tempNodeOne
            tempNodeOne = tempNodeOne.next
        tempNode = tempNode.next
    if not tempNodeOne:
        # tempNodeOne没有了，剩下的tempNodeTwo接上
        tempNode.next = tempNodeTwo
        pass
    if not tempNodeTwo:
        # tempNodeTwo没有了，剩下的tempNodeOne接上
        tempNode.next = tempNodeOne
    linkListRes.size = linkListOne.size + linkListTwo.size
    return linkListRes


def findMiddleNode(singleLinkList):  # 求单链表的中间节点
    if not singleLinkList or not singleLinkList.head.next:
        return -1
    size = singleLinkList.size
    if size % 2 == 0:
        index = int(size / 2)
    else:
        index = size // 2 + 1
    return singleLinkList.find(index)


def delReverseNNode(singleLinkList, n):  # 删除链表中倒数第n个节点
    if n <= 0 or n > singleLinkList.size:
        raise ValueError('n is out of range!')
    preNNodeIndex = singleLinkList.size - n  # 找到倒数第n个节点的前一个节点
    preNNode = singleLinkList.find(preNNodeIndex)
    preNNode.next = preNNode.next.next


if __name__ == '__main__':
    singleLinkList1 = SingleLinkList()
    singleLinkList2 = SingleLinkList()
    singleLinkList1.insertLast(1)
    singleLinkList1.insertLast(3)
    singleLinkList1.insertLast(5)
    singleLinkList2.insertLast(2)
    singleLinkList2.insertLast(4)
    singleLinkList2.insertLast(6)
    singleLinkList2.insertLast(8)
    singleLinkList2.insertLast(10)
    linkList = sortLinkListMerage(linkListOne=singleLinkList1, linkListTwo=singleLinkList2)
    print(linkList)


    # delReverseNNode(singleLinkList, 2)
    # print(singleLinkList)
    # print(singleLinkList)
    # reverse(singleLinkList)
    # print(singleLinkList)
    # singleLinkList.changeToCycle()
    # print(isCycleLinkList(singleLinkList))


